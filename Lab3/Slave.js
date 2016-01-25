function generateWords(num){
    var Slave = "Yoda, mówi, po, polsku,"
    var words = Slave.split(" ");
    var word = "";

    for (var i = 0; i < num; i++){
        var rand = parseInt(Math.random() * words.length);
        word += " " + words[rand];
    }
    return word;
}

// @arg data[num] int The number of words to generate
self.onmessage = function(event) {
    var word = generateWords(event.data.num);
    self.postMessage({Slave: word});
}