chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
      const url = details.url;
  
      fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: JSON.stringify({ URL: url }),
        headers: { 'Content-Type': 'application/json' }
      })
      .then(response => response.json())
      .then(data => {
        if (data.malicious) {
          chrome.tabs.update(details.tabId, { url: "warning.html" });
        }
      })
      .catch(err => console.error('API Error:', err));
  
      return { cancel: false };
    },
    { urls: ["<all_urls>"] },
    ["blocking"]
  );