chrome.runtime.onInstalled.addListener(function() {
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    chrome.declarativeContent.onPageChanged.addRules([{
      conditions: [
        new chrome.declarativeContent.PageStateMatcher({
          pageUrl: {hostContains: 'developer.chrome.com'},
        }),
        // When a page contains a <video> tag...
        new chrome.declarativeContent.PageStateMatcher({
          css: ["video"]
        })
      ],
      actions: [new chrome.declarativeContent.ShowPageAction()]
    }]);
  });
});

chrome.commands.onCommand.addListener(function(command) {
  console.log('Command:', command);
});