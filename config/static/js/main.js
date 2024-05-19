setTimeout(function() {
    var message = document.getElementById('message1');
    if (message) {
        message.style.transition = 'opacity 1s';
        message.style.opacity = '0';
        setTimeout(function() {
            message.style.display = 'none';
        }, 1000);
    }
}, 3000);