export async function analyzeImage({ imageUrl, prompt, analysisType = 'full' }) {
  const response = await fetch('http://localhost:3001/api/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ imageUrl, prompt, analysisType })
  });

  if (!response.ok) {
    throw new Error('Image analysis failed');
  }

  return response.json();
}

export async function exportImage({ format = 'png', quality = 0.92 }) {
  const response = await fetch('http://localhost:3001/api/export', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ format, quality })
  });

  if (!response.ok) {
    throw new Error('Image export failed');
  }

  return response.json();
}
