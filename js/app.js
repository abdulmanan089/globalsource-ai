function findSuppliers(){

let product=document.getElementById("product").value.toLowerCase()

fetch("database/suppliers.json")

.then(res=>res.json())

.then(data=>{

let result=""

data.forEach(supplier=>{

if(supplier.product.includes(product)){

result +=`

<div class="card">

<h3>${supplier.name}</h3>

<p>Country: ${supplier.country}</p>

<p>Price: $${supplier.price}</p>

<button>Contact Supplier</button>

</div>

`

}

})

document.getElementById("results").innerHTML=result

})

}