var btn = document.getElementById("modeButton");

function setMode() {
    var mode = localStorage.getItem("mode");
    if(mode == "Dark Mode") {
        document.body.style.backgroundColor = '#ffffff';
        document.getElementById("topHeader").style.backgroundColor = '#ffffff';
        document.getElementById("covidInfoTab").style.backgroundColor = '#ffffff';
        document.getElementById("covidInfoTab").style.color = '#000000';
        btn.innerHTML = "Dark Mode";
    } else {
        document.body.style.backgroundColor = '#000000';
        document.getElementById("topHeader").style.backgroundColor = '#000000';
        document.getElementById("covidInfoTab").style.backgroundColor = '#000000';
        document.getElementById("covidInfoTab").style.color = '#ffffff';
        btn.innerHTML = "Light Mode";
    }
}

function changeMode(btn) {
    if(btn.innerHTML == "Dark Mode") {
        document.body.style.backgroundColor = '#000000';
        document.getElementById("topHeader").style.backgroundColor = '#000000';
        document.getElementById("covidInfoTab").style.backgroundColor = '#000000';
        document.getElementById("covidInfoTab").style.color = '#ffffff';
        btn.innerHTML = "Light Mode";
        localStorage.setItem("mode", "Light Mode");
    } else{
        document.body.style.backgroundColor = '#ffffff';
        document.getElementById("topHeader").style.backgroundColor = '#ffffff';
        document.getElementById("covidInfoTab").style.backgroundColor = '#ffffff';
        document.getElementById("covidInfoTab").style.color = '#000000';
        btn.innerHTML = "Dark Mode";
        localStorage.setItem("mode", "Dark Mode");
    }
}    
