// was used to refactor the vocab-list to give it also the "Fragen:..., Antwort:..." Schema"

let fragen = require("./fragen.json");
let fs = require("fs");

function createQuestionAnswerFormat(data) {
    let questionAnswer = Object.entries(data).map(([frage, antwort]) => {
        let obj = {};
        obj["Frage"] = frage;
        obj["Antwort"] = antwort;
        return obj;
    });
    console.log(questionAnswer);
    return questionAnswer;
}

let vokabeln = createQuestionAnswerFormat(fragen);
console.log(vokabeln);

// commented out it does not accidently overwrite something
//fs.writeFile("./vokabeln.json", JSON.stringify(vokabeln));