// console.log("Hello, world!");


// console.log("Naam: Chandni");
// console.log("Path: ", __filename);
// console.log("Directory: ", __dirname);
// console.log("OS: ", process.platform);


// const fs = require('fs');

// // ✅ File create + write
// fs.writeFileSync('demo.txt', 'Hello from Node.js file system!'); // ek nayi file banata hai

// // ✅ File read
// const data = fs.readFileSync('demo.txt', 'utf8'); // file padh raha hai
// console.log(data); // console pe output de raha hai


/*
const fs = require('fs');

// Function to write first note
function writeNotes(note){
    fs.writeFileSync('notes.txt', note+'\n','utf-8');
    console.log('✅ Note added!');
}
// Function to add more notes (append)
function addNotes(note){
    fs.appendFileSync('notes.txt', note+'\n', 'utf-8');
    console.log('✅ Note added!');
}
// Function to read all notes
function readNotes(){
    data=fs.readFileSync('notes.txt','utf-8');
    console.log('\n Your Notes:\n--------------\n' + data);
}

writeNotes('Node.js sikhna start kar diya hai!');
addNotes('Aaj writeFileSync aur appendFileSync samjha.');
addNotes('Kal http module karenge.');
readNotes();
*/