const nos = [
    "QUEST1",
    "QUEST2",
    "QUEST3",
    "QUEST4",
    "QUEST5",
    "QUEST6",
    "QUEST7",
    "QUEST8",
    "QUEST9",
    "QUEST10",
    "QUEST11",
    "QUEST12",
    "QUEST13",
    "QUEST14",
    "QUEST15",
    "QUEST16",
    "QUEST17",
    "QUEST18",
    "QUEST19",
    "QUEST20",
  ];

  const grafo = [
["QUEST20", "QUEST17", "QUEST16"],
["QUEST18", "QUEST14", "QUEST7", "QUEST6"],
["QUEST15", "QUEST14", "QUEST4"],
["QUEST11", "QUEST3"],
["QUEST8"],
["QUEST16", "QUEST2"],
["QUEST2"],
["QUEST18", "QUEST5"],
["QUEST19", "QUEST12"],
["QUEST17", "QUEST11"],
["QUEST10", "QUEST4"],
["QUEST9"],
["QUEST20", "QUEST16"],
["QUEST15", "QUEST3", "QUEST2"],
["QUEST16", "QUEST14", "QUEST3"],
["QUEST15", "QUEST13", "QUEST6", "QUEST1"],
["QUEST10", "QUEST1"],
["QUEST19", "QUEST8", "QUEST2"],
["QUEST18", "QUEST9"],
["QUEST13", "QUEST1"]
];


  //    const nos = {{ nos_ | tojson | safe }};
  //     const grafo = {{ grafo_ | tojson | safe }};
  //     const resultado = {{ caminho | tojson | safe }};

  // Mapeia os nós para objetos Node
  const nodes = nos.map((nodeName) => ({
    id: nodeName,
  }));

  // Cria um mapa para procurar nós por id
  const nodeMap = new Map(nodes.map((node) => [node.id, node]));

  // Monta as conexões
  const links = [];
  nos.forEach((origem, index) => {
    const conexoes = grafo[index];
    conexoes.forEach((destino) => {
      const sourceNode = nodeMap.get(origem);
      const targetNode = nodeMap.get(destino);
      if (sourceNode && targetNode) {
        links.push({ source: sourceNode, target: targetNode });
      }
    });
  });

  const svg = d3.select("#graph");
  const simulation = d3
    .forceSimulation(nodes)
    .force(
      "link",
      d3
        .forceLink(links)
        .id((d) => d.id)
        .distance(10) // Ajuste a distância aqui
    )
    .force("charge", d3.forceManyBody().strength(-450))
    .force(
      "center",
      d3.forceCenter(svg.attr("width") / 2, svg.attr("height") / 2)
    );

  const link = svg
    .selectAll(".link")
    .data(links)
    .enter()
    .append("line")
    .attr("class", "link");

  const nodeGroup = svg
    .selectAll(".node")
    .data(nodes)
    .enter()
    .append("g")
    .attr("class", "node")
    .call(
      d3
        .drag()
        .on("start", onDragStart)
        .on("drag", onDrag)
        .on("end", onDragEnd)
    );

  nodeGroup.append("circle").attr("r", 25);

  nodeGroup
    .append("text")
    .attr("class", "node-label")
    .text((d) => d.id);

  function onDragStart(event, d) {
    if (!event.active) simulation.alphaTarget(2.0).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function onDrag(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }

  function onDragEnd(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }

  simulation.on("tick", () => {
    link
      .attr("x1", (d) => d.source.x)
      .attr("y1", (d) => d.source.y)
      .attr("x2", (d) => d.target.x)
      .attr("y2", (d) => d.target.y);

    nodeGroup.attr("transform", (d) => `translate(${d.x},${d.y})`);
  });