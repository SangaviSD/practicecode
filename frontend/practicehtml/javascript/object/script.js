const tech={
    language:"javascript",
    started:"1995",
    creator:"brendan",
    favourite: true,
    idle: null,
}

console.log(tech.language);
tech.about="programming languages";
tech.favourite=false;
delete tech.idle;
console.log(tech);

for ( i in tech){
    console.log(tech[i]);
}
















