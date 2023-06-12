// getting all required elements
const searchWrapper = document.querySelectorAll(".search-input");
const inputBox = document.querySelectorAll("input");
const suggBox = document.querySelectorAll(".autocom-box");
const icon = document.querySelectorAll(".icon");
let linkTag = document.querySelectorAll("a");
const sub_but = document.getElementById("submit")
let webLink;



// console.log(document.querySelectorAll(".search-input"))
// if user press any key and release

console.log(sub_but)

async function send_data(){
    console.log("Button pressed")
    let values = []
    inputBox.forEach((data)=>{
        values.push(data.value)
    })
    console.log(values)



let data = `{
  "Symptoms 1": "${values[0]}",
  "Symptoms 2": "${values[1]}",
  "Symptoms 3": "${values[2]}",
  "Symptoms 4": "${values[3]}",
  "Symptoms 5": "${values[4]}",
}`;
console.log(data)
fetch("http://127.0.0.1:5000/api/predict", {

 method: "POST",
     
    // Adding body or contents to send
    body:  data,
     
    // Adding headers to the request
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
})
.then(response => response.json())
 
// Displaying results to console
.then(json => console.log(json))
.then(()=>{
    window.open("prediction.html")
});


}

inputBox.forEach((ele,index)=>{

    ele.onkeyup = (e)=>{
    let userData = e.target.value; //user enetered data
    let emptyArray = [];
    if(userData){
        console.log(icon)
        icon[index].onclick=()=>{
            // webLink = `https://www.google.com/search?q=${userData}`;
            linkTag[index].setAttribute("href", webLink);
            linkTag[index].click();
            
        }
        emptyArray = suggestions.filter((data)=>{
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            // passing return data inside li tag
            return data = `<li>${data}</li>`;
        });
        searchWrapper[index].classList.add("active"); //show autocomplete box
        showSuggestions(emptyArray,index);
        let allList = suggBox[index].querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", `select(this,${index})`);
        }
    }else{
        searchWrapper[index].classList.remove("active"); //hide autocomplete box
    }
}

})


function select(element,index){
    console.log(element)
    let selectData = element.textContent;
    inputBox[index].value = selectData;
    icon.onclick = ()=>{
        webLink = `https://www.google.com/search?q=${selectData}`;
        linkTag[index].setAttribute("href", webLink);
        linkTag[index].click();
    }
    searchWrapper[index].classList.remove("active");
}

function showSuggestions(list,index){
    let listData;
    if(!list.length){
        userValue = inputBox[index].value;
        listData = `<li>${userValue}</li>`;
    }else{
      listData = list.join('');
    }
    suggBox[index].innerHTML = listData;
}
