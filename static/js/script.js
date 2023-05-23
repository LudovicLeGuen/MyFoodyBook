// function closes the messages after 3 seconds
var message_ele = document.getElementsByClassName("alert");

setTimeout(function(){ 
   message_ele.style.display = "none"; 
}, 3000);