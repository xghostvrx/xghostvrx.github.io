function typeText(element, text, callback) {
    var i = 0;

    function typeCharacter() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(typeCharacter, 50);  // Wait 50ms before typing the next character
        } else if (callback) {
            callback();
        }
    }

    typeCharacter();
}

window.onload = function() {
    const terminal = document.getElementById('terminal');
    const output = document.getElementById('output');
    const input = document.getElementById('input');
    var typing = true;

    var commands = [
        'Loading system files...',
        'Loading user files...',
        'Starting server services...',
        'Activating sentiscore: sentiment analyzer...',
        'System Ready. Type "start" to begin.',
    ];

    var introduction = [
        'This is sentiscore... a sentiment analyzer that uses textBlob to analyze "X" data.',
        'This project is a mock API that simulates a simple sentiment analysis service.',
        'You can interact with the mock API by sending GET requests to a single endpoint.',
        'For example: GET /tweets?ids=1668031228811800000,1668029197065800000',
        'This command will return an empty list of tweets with the given IDs.',
        '-',
        'If you provide additional query parameters, you will get more information.',
        'Copy and paste this, then press enter: GET /tweets?ids=1668031228811800000&tweet.fields=id,created_at,text&user.fields=id,name,username'
    ];

    var i = 0;
    var j = 0;

    function typeNextCommand() {
        if (i < commands.length && typing) {
            var div = document.createElement('div');
            terminal.appendChild(div);
            typeText(div, commands[i], function() {
                i++;
                setTimeout(typeNextCommand, 1000);
            });
        }
    }

    function handleUserInput() {
        var userCommand = input.value;
        var div = document.createElement('div');
        output.appendChild(div);  // Append to the output div instead of the terminal
        typeText(div, '> ' + userCommand, function() {
            input.value = '';

            if (userCommand.toLowerCase() === 'start') {
                typing = false; // Stop typing new commands
                typeNextIntroduction();
            } else if (userCommand.startsWith('GET')) {
                performApiGet(userCommand);
            }
        });
    }

    function typeNextIntroduction() {
        if (j < introduction.length && typing) {
            var div = document.createElement('div');
            terminal.appendChild(div);
            typeText(div, introduction[j], function() {
                j++;
                setTimeout(typeNextIntroduction, 1000);
            });
        }
    }

    function handleUserInput() {
        var userCommand = input.value;
        var div = document.createElement('div');
        terminal.appendChild(div);
        typeText(div, '> ' + userCommand, function() {
            input.value = '';

            if (userCommand.toLowerCase() === 'start') {
                typing = false; // Stop typing new commands
                typeNextIntroduction();
            } else if (userCommand.startsWith('GET')) {
                performApiGet(userCommand);
            }
        });
    }

    input.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            handleUserInput();
        }
    });

    typeNextCommand();

    function performApiGet(command) {
        var apiUrl = 'http://127.0.0.1:5000/' + command.slice(3).trim();
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                var outputDiv = document.createElement('div');
                outputDiv.classList.add('output-div');
                var pre = document.createElement('pre');
                pre.textContent = JSON.stringify(data, null, 2);
                outputDiv.appendChild(pre);
                terminal.appendChild(outputDiv);
                terminal.scrollTop = terminal.scrollHeight;
            })
            .catch(error => {
                var outputDiv = document.createElement('div');
                outputDiv.textContent = 'Error: ' + error;
                terminal.appendChild(outputDiv);
                terminal.scrollTop = terminal.scrollHeight;
            });
    }
}
