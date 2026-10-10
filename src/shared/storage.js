export async function loadImages() {
  const items = await chrome.storage.local.get(['ai-photo-editing-library']);
  return items['ai-photo-editing-library'] || [];
}

export async function addImageToLibrary(image) {
  const existing = await loadImages();
  const next = [...existing, image];
  await chrome.storage.local.set({ 'ai-photo-editing-library': next });
  return next;
}

export async function saveReferenceProfile(profile) {
  const existing = await loadImages();
  await chrome.storage.local.set({ 'reference-profile': profile, 'ai-photo-editing-library': existing });
}
