$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        console.log("here")
        var searchText = $('#searchbar').val();
        $.ajax({
            url: '/ghost?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                console.log(resp.data);
                var newHtml = resp.data.map(d => {
                    return `<div class="well-ghost">
                        <a href="/ghost/${d.id}">
                            <img class="ghost-img" src="${d.image}" />
                            <h4>${d.name}</h4>
                            <p>${d.price}</p>
                        </a>
                    </div>`
                });
                $('.Pizzas').html(newHtml.join(''));
                $('#searchbar').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    })
})

$(document).ready(function(){
    $(".filter-button").click(function(){
        var value = $(this).attr('data-filter');

        if(value == "all")
        {
            $('.Pizzas .well-ghost').show('1000');
        }
        else
        {
            $('.Pizzas .well-ghost').not('.'+value).hide('3000');
            $('.Pizzas .well-ghost').filter('.'+value).show('3000');
        }
    });
});

$(document).ready(function(){
    $("#search-btn").click(function(){
        var value = $("#searchbar").val().toLowerCase();

        $(".Pizzas .well-ghost").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("#sort-by-value-btn").click(function(){
        var sortedPizzas = $(".Pizzas .well-ghost").sort(function(a, b){
            return parseInt($(b).data("value")) - parseInt($(a).data("value"));
        });

        $(".Pizzas").empty().append(sortedPizzas);
    });

    $("#sort-by-price-btn").click(function(){
        var sortedPizzas = $(".Pizzas .well-ghost").sort(function(a, b){
            return parseFloat($(a).data("price")) - parseFloat($(b).data("price"));
        });

        $(".Pizzas").empty().append(sortedPizzas);
    });
});
