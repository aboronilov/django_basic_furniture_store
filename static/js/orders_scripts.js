function recalculate_total_values () {
    var quantities = [];
    var prices = [];

    TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());

//    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
//    var order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

    for (var i=0; i < TOTAL_FORMS; i++) {
       _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
       _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));

       quantities[i] = _quantity;

       if (_price) {
           prices[i] = _price;
       } else {
           prices[i] = 0;
       }
    }

    order_total_quantity = 0;
    order_total_cost = 0;

    for (var i=0; i < TOTAL_FORMS; i++) {
       order_total_quantity += quantities[i];
       order_total_cost += quantities[i] * prices[i];

   $('.order_total_quantity').text(order_total_quantity).toFixed(2);
   $('.order_total_cost').text(order_total_cost);
}
    window.onload = function() {
        $('.order_form input[type="number"]').on('click', recalculate_total_values)
    recalculate_total_values()
}

}


//function deleteOrderItem(row) {
//   var target_name= row[0].querySelector('input[type="number"]').name;
////   orderitem_num = parseInt(target_name.replace('orderitems-', ''). replace('-quantity', ''));
////   delta_quantity = -quantity_arr[orderitem_num];
//   recalculate_total_values()
//}


