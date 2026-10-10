import { analyzeImage, exportImage } from '../shared/api.js';
import { loadImages, addImageToLibrary } from '../shared/storage.js';

const imageUrlInput = document.getElementById('imageUrl');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultBox = document.getElementById('result');

async function handleAnalyze() {
  const imageUrl = imageUrlInput.value.trim();

  if (!imageUrl) {
    resultBox.textContent = 'Please enter an image URL or use a captured image.';
    return;
  }

  resultBox.textContent = 'Analyzing image...';

  try {
    const response = await analyzeImage({
      imageUrl,
      prompt: 'Analyze subject, mood, lighting, and draw out a professional retouching plan.',
      analysisType: 'full'
    });

    const profile = response.result ?? response;
    resultBox.innerHTML = `
      <strong>Subject:</strong> ${profile.subject}<br />
      <strong>Mood:</strong> ${profile.mood}<br />
      <strong>Lighting:</strong> ${profile.lighting}<br />
      <strong>Style:</strong> ${profile.style}<br />
      <strong>Suggestions:</strong> ${profile.recommendations?.join(', ') || 'None'}
    `;

    await addImageToLibrary({
      id: crypto.randomUUID(),
      name: 'reference-image',
      url: imageUrl,
      timestamp: Date.now()
    });
  } catch (error) {
    resultBox.textContent = error instanceof Error ? error.message : 'Analysis failed.';
  }
}

analyzeBtn.addEventListener('click', handleAnalyze);

document.querySelectorAll('[data-action]').forEach((button) => {
  button.addEventListener('click', async () => {
    const action = button.getAttribute('data-action');

    if (action === 'capture') {
      const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
      const currentTab = tabs[0];
      if (currentTab?.id) {
        chrome.tabs.sendMessage(currentTab.id, { type: 'CAPTURE_IMAGE' });
        resultBox.textContent = 'Capture request sent to page.';
      }
    }

    if (action === 'reference') {
      const images = await loadImages();
      resultBox.textContent = `Saved references: ${images.length}`;
    }

    if (action === 'export') {
      const output = await exportImage({ format: 'png', quality: 0.92 });
      resultBox.textContent = `Export ready: ${output.output.filename}`;
    }
  });
});
