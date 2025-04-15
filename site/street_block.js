const myBlock = document.getElementById('output');
    const text = myBlock.innerText; // Получаем текст из блока
    const textLength = text.length; // Получаем длину строки

    // Устанавливаем ширину блока в зависимости от длины строки
    const widthPerCharacter = 10; // Ширина одного символа в px
    myBlock.index.width = (textLength * widthPerCharacter) + 'px';