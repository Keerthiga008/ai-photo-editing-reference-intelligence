chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message.type === 'CAPTURE_IMAGE') {
    const images = Array.from(document.querySelectorAll('img'));
    const img = images[0];
    if (img?.src) {
      sendResponse({ ok: true, imageUrl: img.src });
      return true;
    }

    sendResponse({ ok: false, message: 'No image found on this page.' });
    return true;
  }

  return false;
});

const injectedScript = document.createElement('script');
injectedScript.src = chrome.runtime.getURL('src/injected/injected-script.js');
document.documentElement.appendChild(injectedScript);
