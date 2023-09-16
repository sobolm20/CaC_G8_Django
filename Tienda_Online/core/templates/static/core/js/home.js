from products import productos 

let data = productos [] 

async function fetchApi() {
    try{
        let urlApi = data
        let fetchResponse = await fetch(urlApi)
        let response = await fetchResponse.json()
        productos = [...response.meals]
        console.log(productos);
        printCards('allprods',response.meals)
        return response
    } catch(error){
        console.log(error);
    }
}

fetchApi()

let cardprod = []

function printCards(){
    for (let card of productos){
            let listcard = 
            `
            <div class="card" style="width: 16rem">
                <img src=${card.imagen} class="img-fit" alt=${card.articulo}>
                <div>
                    <h2>${card.articulo}</h2>
                    <h3>${card.Categoria}</h3>
                    <a class="btnd" href="details.html?id=${card.articulo}" role="button">Details</a>
                </div>
            </div>
            `

            cardprod.push(listcard);
            console.log(cardprod);
    }
    let basecard = document.getElementById('allprods');
    basecard.innerHTML = cardprod.join('');
}

printCards();