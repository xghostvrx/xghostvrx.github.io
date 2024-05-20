$(document).ready(function() {
    $('#terminal').terminal(function(command, term) {
        if (command !== '') {
            if (command == 'init') {
                typeText(this, 'Loading introduction...', 100, function() {
                    term.set_command('');
                });
                introduction(term);
            } else if (command == 'options') {
                options(term);
            } else if (command == 'list') {
                list(term);
            } else if (command == 'help') {
                help(term);
            } else if (command == 'query') {
                example_query(term);
            } else if (command.startsWith('GET ')) {
                const url = command.substring(4);
                curlGet(url, term);
                term.echo(url);
            }
        } else {
            term.echo('');
        }
    }, {
        greetings: 'Initializing startup sequence...',
        onInit: function(term) {
            term.disable();
            setTimeout(function() {
                term.echo('Loading core modules...');
                setTimeout(function() {
                    term.echo('Starting services...');
                    setTimeout(function() {
                        term.echo('Running sentiscore...');
                        setTimeout(function() {
                            term.echo('System check complete.');
                            setTimeout(function() {
                                term.echo('Type "init" for introduction.');
                                term.enable();
                                term.set_prompt('> ');
                            }, 1000);
                        }, 1000);
                    }, 1000);
                }, 1000);
            }, 1000);
        },
        prompt: '',
        name: 'js_terminal',
        height: '100%',
        width: '100%',
        prompt: ''
    });
});

function introduction(term) {
    term.disable();
    setTimeout(function() {
        term.echo('Sentiscore is a sentiment analyzer that uses a Python library called "textBlob" to analyze data.');
        setTimeout(function() {
            term.echo('This personal project consists of a mock API that simulates a simple sentiment analysis service.');
            setTimeout(function() {
                term.echo('You can interact with the application by sending GET requests to /tweets.');
                setTimeout(function() {
                    term.echo('For example: GET /tweets?ids=1668031228811800000&tweet.fields=text');
                    setTimeout(function() {
                        term.echo('This command will return a list with the given tweet ID and text.');
                        setTimeout(function() {
                            term.echo('Type "options" to continue.');
                            term.enable();
                            term.set_prompt('> ');
                        }, 3000);
                    }, 3000);
                }, 3000);
            }, 3000);
        }, 3000);
    }, 3000);
}
function options(term) {
    var acceptable_args = {
        'ids': '19-character string representing the unique identifier of a tweet',
        'tweet.fields': ['author_id', 'created_at', 'id', 'text'],
        'user.fields': ['created_at', 'description', 'id', 'name', 'username']
    };

    term.echo('Acceptable keys and their values:');
    $.each(acceptable_args, function(key, value) {
        term.echo(key + ': ' + (Array.isArray(value) ? value.join(', ') : value));
    });

    term.echo('\nHow to use the "GET" request command:');
    term.echo('GET /tweets?ids=<id>&tweet.fields=<tweet_value>&user.fields=<user_value>');
    term.echo('Replace <id>, <tweet_value>, and <user_value> with your desired values from the acceptable keys and values above.');

    term.echo('\nAvailable commands:');
    term.echo('init: Provides a quick introduction to the application');
    term.echo('options: Display the acceptable keys and their values');
    term.echo('GET /tweets: Retrieve tweets based on specific parameters (as shown above as acceptable "keys" and "values")');
    term.echo('list: Displays a list of available tweets ids to use as a query');
    term.echo('help: Provides a brief explanation of query parameters and how they work');

    term.echo('\nFor an example command to use, please type "query"');
}

function list(term) {
    var ids = ['1668031228811800000','1668029197065800000','1668017215944130000','1668014822326140000','1668013802359490000','1668013122567780000','1668012189955810000','1668011771532040000','1668011185248120000','1668009508633750000','1668008743328510000','1668006873604280000','1668006548335930000','1668005894326480000','1668004568637080000','1668003032259260000','1667999474684390000','1667996790036000000','1667992787885620000','1667982248614730000'];
    $.each(ids, function(index, id) {
        term.echo(id);
    });
}

function help(term) {
    term.disable();
    setTimeout(function() {
        term.echo('Query parameters are a defined set of parameters attached to the end of a URL.')
        setTimeout(function() {
            term.echo('They are extensions of the URL that are used to help define specific content or actions based on the data.')
            setTimeout(function() {
                term.echo('To add query parameters to a URL, you start with a question mark "?". Then you append the key and the value with an equal sign "=" between them. If you want to add multiple query parameters, you separate them with an ampersand "&".')
                setTimeout(function() {
                    term.echo('For example, in the command GET /tweets?param1=value1&param2=value2, "param1" and "param2" are keys and "value1" and "value2" are their values.')
                    setTimeout(function() {
                        term.echo('In the context of this application, query parameters are used to specify data that should be returned. The keys (ids, tweet.fields, user.fields) specify the type of data, and the values (id, created_at, text, name, username) specify the specific fields of data.')
                    }, 2000)
                }, 2000)
            }, 2000)
        }, 2000);
    }, 1000);
}

function example_query(term) {
    var command = 'GET /tweets?ids=1668031228811800000,1668029197065800000,1668017215944130000,1668014822326140000,1668013802359490000,1668013122567780000,1668012189955810000,1668011771532040000,1668011185248120000,1668009508633750000,1668008743328510000,1668006873604280000,1668006548335930000,1668005894326480000,1668004568637080000,1668003032259260000,1667999474684390000,1667996790036000000,1667992787885620000,1667982248614730000&tweet.fields=id,created_at,author_id,text&user.fields=id,name,username,description';
    term.echo(command);
}

function typeText(term, text, delay, callback) {
    let i = 0;
    let intervalId = setInterval(function() {
        term.set_command(term.get_command() + text[i]);
        i++;
        if (i === text.length) {
            clearInterval(intervalId);
            term.exec(text);
            if (callback) callback();
        }
    }, delay);
}

function curlGet(url, term) {
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            term.echo(JSON.stringify(data, null, 2));
        },
        error: function(jqXHR, textStatus, errorThrown) {
            term.error('Error: ' + textStatus + ' ' + errorThrown);
        }
    });
}
