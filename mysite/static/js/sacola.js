document.querySelectorAll('button[name="btn"').forEach(
    function(button){
        button.addEventListener('click', function(event){
            let btn = event.target || event.srcElement;
            while (btn.className != "produto m-4"){
                btn = btn.parentElement
            }
            let produtos = btn.parentElement
            btn.remove()
            checkProdutos(produtos)
        })
    }
)
function checkProdutos(produtos) {
    if (produtos.childElementCount == 0)
    {
        let container = document.createElement('div')
        let message = document.createElement('h1')
        container.append(message)
        container.className = 'd-flex justify-content-center align-items-center '
        container.style.height = '100%'
        message.innerText = 'Nenhum produto na sacola'
        produtos.append(container)
    }    
}


function minus() {
    let total = document.querySelector(".valor")
    console.log(total.textContent)
    if (!total.innerHTML == "0"){
        total.innerHTML = parseInt(total.innerHTML) - 1

    }
    
}

function plus() {
    let total = document.querySelector(".valor")
    if (!total.innerHTML == "0"){
        total.innerHTML = parseInt(total.innerHTML) + 1

    }

}