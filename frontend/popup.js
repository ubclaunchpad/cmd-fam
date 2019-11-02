chrome.storage.sync.get('keyword', function(data) {
  searchInput.value = data.keyword;
  searchInput.setAttribute('value', data.keyword);
});

document.getElementById('searchInput').addEventListener(
  'change',
  function (evt) {
    chrome.storage.sync.set({
      keyword: this.value
    }, function() {
      console.log("The keyword: " + this.value);
    });
  },
  false
);


next.onclick = function(element) {
  alert("next");
};

previous.onclick = function(element) {
  alert("previous");
};

clear.onclick = function(element) {
  chrome.storage.sync.set({
    keyword: ""
  }, function() {
    console.log("The keyword: empty");
  });
  document.getElementById("searchInput").value = "";
  document.getElementById("searchInput").focus();
};