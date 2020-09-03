const Discord = require('discord.js');
const path = require('path');

module.exports = {
  name: 'umu',
  description: 'Umu!',
  cooldown: 5,
  getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
  },
  execute(message) {
    const files = ['nero01.png', 'nero02.png', 'nero03.jpg', 'nero04.png'];
    const index = this.getRandomNumber(0, 3);

    const embedMessage = new Discord.MessageEmbed()
      .setTitle('Nero!!')
      .attachFiles([path.join(__dirname, `./../assets/${files[index]}`)])
      .setImage(`attachment://${files[index]}`);
    message.channel.send(embedMessage);
  },
};
