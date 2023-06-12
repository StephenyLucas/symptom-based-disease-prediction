
  
const charactersList = document.getElementById('charactersList');
let hpCharacters = [];
var latitude
var longitude
navigator.geolocation.getCurrentPosition(function(position){
        
        latitude=position.coords.latitude;
        longitude=position.coords.longitude;
        console.log(latitude,longitude);
        loadCharacters(latitude,longitude);



    });



const loadCharacters = async (latitude,longitude) => {
    

    try {

        const res = await fetch(`https://places.ls.hereapi.com/places/v1/discover/search?apiKey=bfmwzMkMICuI1AI-j4JOw-KweUGN0I5iaw2Ph-kDoJA&in=${latitude},${longitude};r=1000&q=hospital&result_types=address,query`);
        hpCharacters = await res.json();
        console.log(hpCharacters)
        displayCharacters(hpCharacters);
    } catch (err) {
        console.error(err);
    }
};

const displayCharacters = (characters) => {

    
        const htmlString = characters.results.items.map((character) => {


            return `

            <li class="character">
            <a href="https://www.google.com/search?q=${character.title} ${character.vicinity}">
                <h2>${character.title}</h2>
                <p>House: ${character.vicinity}</p>
                <p>Distance:  ${character.distance}</p>
                <img src="${character.icon}"></img>
            </a>
            </li>
        `;
        })
        .join('');
    charactersList.innerHTML = htmlString;
};