$('.main-slider').slick({
  infinite: true,
  arrows: false,
});

$('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    dots: false,
    arrows: true,
    focusOnSelect: true,
    centerMode: true,
    infinite: true,
    variableWidth: true

});


$('document').ready(function(){
    var update_q = $('.update_q');

    update_q.on('input', function(e){
        var form = $(this).parent('form');
        var id = form.attr('id').split('--')[1];
        console.log(id);

        $.ajax({
            url : form.attr('action'),
            type : "POST",
            data : form.serialize(),

            success: function(json){
                $('#sum--' + id).text(json.sum);
                $('.cart-sum').text(json.cart_sum);
            },
            error: function(e){
                console.log(e);
            }
        });

    });


});



// number spinner
(function($) {
	$.fn.spinner = function() {
		this.each(function() {
			var el = $(this);

			// add elements
			// el.wrap('<span class="spinner"></span>');
			// el.before('<span class="sub">-</span>');
			// el.after('<span class="add">+</span>');

			// substract
			el.parent().on('click', '.sub', function () {
				if (el.val() > parseInt(el.attr('min')))
					el.val( function(i, oldval) { return --oldval; });
			});

			// increment
			el.parent().on('click', '.add', function () {
				if (el.val() < parseInt(el.attr('max')))
					el.val( function(i, oldval) { return ++oldval; });
			});
	    });
	};
})(jQuery);

$('input[type=number]').spinner();


// Accordion

var accordion = (function (element) {

var _getItem = function (elements, className) {
var element = undefined;
elements.forEach(function (item) {
	if (item.classList.contains(className)) {
        element = item;
        }
 });
     return element;
};

return function () {
  var _mainElement = {},
    _items = {},
 _contents = {};

var _actionClick = function (e) {
    if (!e.target.classList.contains('accordion-item-header')) {
        return;
}
e.preventDefault();

var header = e.target,
item = header.parentElement,
itemActive = _getItem(_items, 'show');

if (itemActive === undefined) {
    item.classList.add('show');
} else {

itemActive.classList.remove('show');

 if (itemActive !== item) {

    item.classList.add('show');
		}
    }
},
_setupListeners = function () {

    _mainElement.addEventListener('click', _actionClick);
 };

return {
   init: function (element) {
    _mainElement = (typeof element === 'string' ? document.querySelector(element) : element);
    _items = _mainElement.querySelectorAll('.accordion-item');
    _setupListeners();
		}
    }
 }
 })();


var accordion1 = accordion();
accordion1.init('#accordion');

