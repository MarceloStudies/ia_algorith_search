$(function () {

    const perguntas = {
      "QUEST1": "O que é um algoritmo?",
      "QUEST2": "O que são variáveis em programação?",
      "QUEST3": "Explique o que são estruturas de controle em programação.",
      "QUEST4": "O que é uma estrutura de repetição?",
      "QUEST5": "O que são arrays e como são usadas?",
      "QUEST6": "Qual é a diferença entre '==' e '===' em JavaScript?",
      "QUEST7": "Explique o que é recursão em programação.",
      "QUEST8": "O que é uma função de ordem superior?",
      "QUEST9": "O que são algoritmos de ordenação e dê exemplos.",
      "QUEST10": "O que é complexidade de tempo e espaço em algoritmos?",
      "QUEST11": "O que é orientação a objetos?",
      "QUEST12": "Explique encapsulamento em programação orientada a objetos.",
      "QUEST13": "O que é herança em programação orientada a objetos?",
      "QUEST14": "Explique polimorfismo em programação orientada a objetos.",
      "QUEST15": "O que são exceções em programação?",
      "QUEST16": "O que é desenvolvimento ágil?",
      "QUEST17": "O que é Git e como é usado no desenvolvimento de software?",
      "QUEST18": "Explique o que é API (Interface de Programação de Aplicações).",
      "QUEST19": "O que é CRUD em sistemas de informação?",
      "QUEST20": "O que é teste unitário e por que é importante?"
    };

    $('#metodo').on('change', function(){
      if($(this).val() == 4){
        $("#limit").attr("hidden", false)
      }else{
        $("#limit").attr("hidden", true)
      }
    })

    $("#enviar").on('click', function (e) {

      var ini = $("#ini").val();
      var fim = $("#fim").val();
      var tipo = $("#metodo").val();
      var limit = $("#limit").val();
      if (limit == '' || limit == null){
        limit = '1' ;
      }

      $.ajax({
        url: "http://localhost:5000/api/exemplo", // Substitua pelo URL da sua API Flask se estiver em um servidor diferente
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ inicio: ini, final: fim, tipo: parseInt(tipo), limit: parseInt(limit) }),
        success: function (response) {
          $(".list-quest").empty()

          console.table(response)
          let array = response.caminho;
          array.forEach(element => {
          $(".list-quest").append(`
          <li class="text-quest">
            <span class = "font-head">${element}</span>
            <span>${perguntas[element]}</span>
          </li>
          `)
         });
        },
        error: function (xhr, status, error) {
          // Manipule erros aqui
          console.log("Erro na requisição:", status, error);
        },
      });
    })
  });