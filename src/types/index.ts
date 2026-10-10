// Image & Reference Types
export interface ImageData {
  id: string;
  url: string;
  dataUrl?: string;
  name: string;
  timestamp: number;
  width?: number;
  height?: number;
  metadata?: ImageMetadata;
}

export interface ImageMetadata {
  subjects?: string[];
  lighting?: string;
  mood?: string;
  colorPalette?: string[];
  style?: string;
  tags?: string[];
}

// Analysis Types
export interface AnalysisRequest {
  imageDataUrl: string;
  analysisType: 'full' | 'subject' | 'lighting' | 'color';
}

export interface AnalysisResult {
  id: string;
  imageId: string;
  subjects: SubjectClassification[];
  lighting: LightingAnalysis;
  colorPalette: ColorAnalysis;
  style: StyleAnalysis;
  mood: string;
  recommendations: string[];
  timestamp: number;
}

export interface SubjectClassification {
  category: 'portrait' | 'couple' | 'group' | 'landscape' | 'product' | 'event' | 'other';
  confidence: number;
  details: string;
}

export interface LightingAnalysis {
  type: string; // 'natural', 'studio', 'mixed', etc.
  direction: string;
  intensity: 'low' | 'medium' | 'high';
  quality: string;
  suggestions: string[];
}

export interface ColorAnalysis {
  dominantColors: Array<{ hex: string; label: string; percentage: number }>;
  mood: string;
  suggestions: string[];
}

export interface StyleAnalysis {
  aesthetic: string;
  treatment: string;
  colorGrade: string;
}

// Editing Plan Types
export interface EditingPlan {
  id: string;
  imageId: string;
  analysisId: string;
  referenceId?: string;
  title: string;
  steps: EditingStep[];
  exposureCorrection?: ExposureSettings;
  whiteBalance?: WhiteBalanceSettings;
  colorCorrection?: ColorCorrectionSettings;
  skinRetouching?: SkinRetouchingSettings;
  detailEnhancement?: DetailSettings;
  created: number;
  updated: number;
}

export interface EditingStep {
  id: string;
  order: number;
  category: 'exposure' | 'white_balance' | 'color' | 'skin' | 'detail' | 'custom';
  description: string;
  settings: Record<string, any>;
  priority: 'high' | 'medium' | 'low';
}

export interface ExposureSettings {
  exposure?: number;
  highlights?: number;
  shadows?: number;
  whitePoint?: number;
  blackPoint?: number;
}

export interface WhiteBalanceSettings {
  temperature?: number;
  tint?: number;
  colorTemperature?: 'daylight' | 'cloudy' | 'shade' | 'tungsten' | 'fluorescent';
}

export interface ColorCorrectionSettings {
  saturation?: number;
  vibrance?: number;
  hue?: Record<string, number>;
  curves?: Array<{ input: number; output: number }>;
}

export interface SkinRetouchingSettings {
  smoothing?: number;
  clarity?: number;
  texture?: number;
  blemishRemoval?: boolean;
}

export interface DetailSettings {
  sharpness?: number;
  clarity?: number;
  dehazeAmount?: number;
  noiseSuppression?: number;
}

// Reference Profile Types
export interface ReferenceProfile {
  id: string;
  name: string;
  images: string[]; // Image IDs
  metadata: ImageMetadata;
  style: string;
  mood: string;
  colorPalette: string[];
  created: number;
  updated: number;
  tags: string[];
}

// Project Types
export interface Project {
  id: string;
  name: string;
  description?: string;
  images: string[]; // Image IDs
  referenceProfiles: string[]; // Reference Profile IDs
  editingPlans: string[]; // Editing Plan IDs
  created: number;
  updated: number;
  status: 'draft' | 'in_progress' | 'completed';
}

// Processing Queue Types
export interface ProcessingJob {
  id: string;
  type: 'analyze' | 'edit' | 'export';
  imageId: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  result?: any;
  error?: string;
  created: number;
  updated: number;
}

// Export Types
export interface ExportSettings {
  format: 'jpg' | 'png' | 'tiff' | 'webp';
  quality?: number;
  width?: number;
  height?: number;
  colorSpace?: 'srgb' | 'adobe_rgb' | 'pro_photo';
  includeMetadata?: boolean;
}

export interface ExportJob extends ProcessingJob {
  type: 'export';
  settings: ExportSettings;
  outputPath?: string;
}

// User Preferences
export interface UserPreferences {
  apiKey: string;
  photoshopIntegrationEnabled: boolean;
  autoSave: boolean;
  defaultQuality: number;
  theme: 'light' | 'dark';
  batchSize: number;
}

// Message Types for Communication
export interface ChromeMessage {
  type: string;
  payload?: any;
}

export interface AnalysisMessage extends ChromeMessage {
  type: 'ANALYZE_IMAGE' | 'ANALYSIS_COMPLETE' | 'ANALYSIS_ERROR';
  payload: {
    imageId?: string;
    imageDataUrl?: string;
    result?: AnalysisResult;
    error?: string;
  };
}

export interface EditingMessage extends ChromeMessage {
  type: 'GENERATE_PLAN' | 'PLAN_READY' | 'APPLY_EDITS' | 'EXPORT_IMAGE';
  payload: {
    imageId?: string;
    analysisId?: string;
    plan?: EditingPlan;
    settings?: ExportSettings;
    result?: string;
    error?: string;
  };
}
