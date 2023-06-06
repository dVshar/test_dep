
function Book_Room(Type){
			
    var Checkin = document.getElementById('checkin_date').value;
    var Checkout = document.getElementById('checkout_date').value;
    var Adult = document.getElementById('adult').value;
    var Kid = document.getElementById('kid').value;
    var Price = document.getElementById('Price_Total').innerHTML;
    var type = Type

    // alert(Price)
    updateUser(Checkin,Checkout, Adult,Kid,Price,type)
        
    function updateUser(Checkin,Checkout, Adult,Kid,Price,type){
        var url="/Encode/"
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({"Checkin":Checkin , "Checkout":Checkout,"Adult":Adult,"Kid":Kid,"Price":Price,"type":type})
        })
        .then((response) =>{
            return response.json()
        })
        .then((data)=>{
            console.log('data',data)
            var token = data["message"]
            window.location.href = `Check/?token=${token}`
        })
        
    
    }
    



}
  