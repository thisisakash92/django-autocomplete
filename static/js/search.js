
    // Bloodhound to search SampleModel
    var sampleModel = new Bloodhound({
    datumTokenizer: function (datum) {
        return Bloodhound.tokenizers.whitespace(datum.name);
    },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    limit: 5, //number of results to display
    remote: { // backend url

        url: 'http://127.0.0.1:8000/search/?q=%QUERY',
        wildcard: '%QUERY',
        filter: function(results) {
            console.log(results)
            return $.map(results, function(result) {
                console.log(result)
                return {
                        name: result.name,
                        url: result.url,

                }
            });
        }
    }
    });
    sampleModel.initialize();

    $('.typeahead').typeahead({
        hint: true,
        highlight: true,
        minLength: 1,

    },
    {
        name: 'SampleModels',
        displayKey: 'name',
                templates: {header: '<h5>Sample Models</h5>',

                    suggestion: Handlebars.compile('<p class="suggested-name"><a href="{{ url }} ">  {{ name }}</a></p>')
                },
        source: sampleModel.ttAdapter()

            }).bind('typeahead:selected', function (obj, datum, name) {
                location.href = datum.url;
            });