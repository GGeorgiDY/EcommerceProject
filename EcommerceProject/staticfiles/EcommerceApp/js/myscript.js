// $('#slider1, #slider2, #slider3').owlCarousel({
//     loop: true,
//     margin: 20,
//     responsiveClass: true,
//     responsive: {
//         0: {
//             items: 2,
//             nav: false,
//             autoplay: true,
//         },
//         600: {
//             items: 4,
//             nav: true,
//             autoplay: true,
//         },
//         1000: {
//             items: 6,
//             nav: true,
//             loop: true,
//             autoplay: true,
//         }
//     }
// })

// var plusCartUrl = "{% url 'plus_cart' %}";

// тук описвам логиката за увеличаване и намаляване на брая поръчки за даден продукт
// като без да се рефрешва страницата, да се увеличават бройките на продуктите при натискане
// на + бутона, както и да се увеличава сумата в кошницата и тотал сумата
$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2];
    var plusCartUrl = $(this).data("plus-url");
    $.ajax({
        type:"GET",
        url:plusCartUrl,
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            location.reload();
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2];
    var minusCartUrl = $(this).data("minus-url");
    $.ajax({
        type:"GET",
        url:minusCartUrl,
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity 
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
            location.reload();
            console.log(location)
        }
    })
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this;
    var removeCartUrl = $(this).data("remove-url");
    $.ajax({
        type:"GET",
        url:removeCartUrl,
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            location.reload();
        }
    })
})


$('.plus-wishlist').click(function(){
    var id = $(this).attr("pid").toString();
    var plusWishlistUrl = $(this).data("plus-wishlist");
    $.ajax({
        type: "GET",
        url: plusWishlistUrl,
        data: {
            prod_id: id
        },
        success: function(data) {
            location.reload();
        }
    });
});

$('.minus-wishlist').click(function(){
    var id = $(this).attr("pid").toString();
    var minusWishlistUrl = $(this).data("minus-wishlist");
    $.ajax({
        type: "GET",
        url: minusWishlistUrl,
        data: {
            prod_id: id
        },
        success: function(data) {
            location.reload();
        }
    });
});