document.getElementById('checkUrl').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      const url = tabs[0].url;
  
      fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: JSON.stringify([{ URL: url }]),
        headers: { 'Content-Type': 'application/json' }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        document.getElementById('result').textContent = data.malicious 
          ? "🚨 Warning! This URL is malicious." 
          : "✅ This URL is safe.";
      })
      .catch(err => {
        console.error('API Error:', err);
        document.getElementById('result').textContent = 'Error fetching data. Please check your backend.';
      });
    });
  });
  