// adds an input field to every question/answer-entry

let questions = require("./vokabeln.json");
let fs = require("fs");

let withInput = questions.map(qa => {
    qa.input = true;
    return qa;
});

// commented out to not overwrite something
//fs.writeFile("./vokabeln.json", JSON.stringify(withInput));