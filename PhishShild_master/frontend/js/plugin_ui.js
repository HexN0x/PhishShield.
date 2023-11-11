var colors = {
    "-1":"#58bc8a", // Legitimate  
    "0":"#ffeb3c",  // Suspicious
    "1":"#ff6666",  // Phishing
};
var featureList = document.getElementById("features");

chrome.tabs.query({ currentWindow: true, active: true }, function(tabs){
    chrome.storage.local.get(['results', 'legitimatePercents', 'isPhish'], function(items) {
        var result = items.results[tabs[0].id];
        var isPhish = items.isPhish[tabs[0].id];
        var legitimatePercent = items.legitimatePercents[tabs[0].id];
    
        for(var key in result){
            var newFeature = document.createElement("li");
            //console.log(key);
            newFeature.textContent = key;
            //newFeature.className = "rounded";
            newFeature.style.backgroundColor=colors[result[key]];
            featureList.appendChild(newFeature);
        }
        
        $("#site_score").text(parseInt(legitimatePercent)+"%");
        if(isPhish) {
            $("#res-circle").css("background", "#ff511a");
            $("#site_msg").text("Warning! You're being phished oooya.");
            $("#site_score").text(parseInt(legitimatePercent)-20+"%");
        }
    });
    
});

