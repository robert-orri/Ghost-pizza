$(document).ready(function() {
    $('#searchbar').on('click', function(e) {
        e.preventDefault();
        const searchText = $('#searchbar').val();
        $.ajax({
            url: '/ghost?search_filter' + searchText,
            type: 'GET',
            success: function(resp) {
                const newHtml = resp.data.map(d => {
                    return '<div class="well-ghost"> ' +
                        <a href="/ghost/${d.id}">

                        </a>
                            '</div>'
                })
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    })
})