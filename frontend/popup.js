chrome.storage.sync.get('keyword', function(data) {
  searchInput.value = data.keyword;
  searchInput.setAttribute('value', data.keyword);
});

chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
  let video_url = tabs[0].url; //TODO: Send this info to server
});

document.getElementById('searchInput').addEventListener(
  'change',
  function (evt) {
    chrome.storage.sync.set({
      keyword: this.value
    }, function() {
      // console.log("The keyword: " + this.value);
    });
  },
  false
);


next.onclick = function(element) {
  alert("next"); //TODO: Add functionality
};

previous.onclick = function(element) {
  alert("previous"); //TODO: Add functionality
};

clear.onclick = function(element) {
  chrome.storage.sync.set({
    keyword: ""
  }, function() {
    // console.log("The keyword: empty");
  });
  document.getElementById("searchInput").value = "";
  document.getElementById("searchInput").focus();
};