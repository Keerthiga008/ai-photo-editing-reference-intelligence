import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import multer from 'multer';

dotenv.config();

const app = express();
const port = process.env.PORT || 3001;

app.use(cors({
  origin: true,
  credentials: true,
}));
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

const upload = multer({ storage: multer.memoryStorage() });

app.get('/health', (_req, res) => {
  res.json({ ok: true, message: 'AI Photo Editing API is running' });
});

app.post('/api/analyze', upload.single('image'), async (req, res) => {
  const { imageUrl, prompt, analysisType } = req.body;

  if (!process.env.GEMINI_API_KEY) {
    return res.status(500).json({
      error: 'GEMINI_API_KEY is not configured',
      note: 'Add your Google Gemini API key to the .env file.'
    });
  }

  try {
    const payload = {
      model: 'gemini-1.5-pro',
      contents: [{
        parts: [
          {
            text: `You are an expert photo editor and visual analyst. Analyze the image and provide a structured response.

Task: ${prompt || 'Analyze this reference image for composition, mood, subject, style, and lighting.'}
Focus on:
- subject detection
- color palette
- lighting and mood
- editing suggestions
- style recommendations
- output as valid JSON only

Return JSON with fields:
{
  subject: string,
  mood: string,
  lighting: string,
  colorPalette: [string],
  style: string,
  recommendations: [string],
  confidence: number
}`
          },
          ...(imageUrl
            ? [{ text: `Image URL: ${imageUrl}` }]
            : [])
        ]
      }]
    };

    // TODO: replace this block with a real Gemini API request using the Google Generative AI SDK or fetch.
    // Example:
    // const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=${process.env.GEMINI_API_KEY}`, {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(payload)
    // });

    res.json({
      ok: true,
      analysisType: analysisType || 'full',
      source: imageUrl ? 'image-url' : 'prompt-only',
      result: {
        subject: 'Portrait',
        mood: 'Warm editorial',
        lighting: 'Natural soft light',
        colorPalette: ['#f5d7c3', '#b2785d', '#5f4b43'],
        style: 'Cinematic natural',
        recommendations: [
          'Slightly lift highlights to preserve skin texture',
          'Add subtle contrast to keep subject separation',
          'Apply controlled warmth for a natural golden-hour look'
        ],
        confidence: 0.92
      }
    });
  } catch (error) {
    console.error('Analyze error:', error);
    res.status(500).json({
      error: 'Failed to analyze image',
      detail: error instanceof Error ? error.message : 'Unknown error'
    });
  }
});

app.post('/api/export', (req, res) => {
  const { format = 'png', quality = 0.92 } = req.body || {};

  // Placeholder export endpoint: this is where a processed image gets exported.
  res.json({
    ok: true,
    message: 'Export request accepted.',
    output: {
      format,
      quality,
      filename: `processed-output.${format}`,
      path: `/exports/processed-output.${format}`
    }
  });
});

app.listen(port, () => {
  console.log(`AI Photo Editing API is running on http://localhost:${port}`);
});
