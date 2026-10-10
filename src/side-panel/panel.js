import { analyzeImage, exportImage } from '../shared/api.js';

const runAnalysisButton = document.getElementById('runAnalysis');
const exportButton = document.getElementById('exportImage');
const openPopupButton = document.getElementById('openPopup');

runAnalysisButton.addEventListener('click', async () => {
  const response = await analyzeImage({
    imageUrl: 'https://images.unsplash.com/...',
    prompt: 'Analyze reference conditions and suggest editing settings for a premium portrait.',
    analysisType: 'full'
  });

  console.log('Analysis result:', response);
  alert(`Analysis ready: ${response.result?.style || 'success'}`);
});

exportButton.addEventListener('click', async () => {
  const response = await exportImage({ format: 'jpg', quality: 0.85 });
  console.log('Export result:', response);
  alert(`Export generated: ${response.output?.filename || 'processed image'}`);
});

openPopupButton.addEventListener('click', () => {
  chrome.runtime.openOptionsPage();
});
