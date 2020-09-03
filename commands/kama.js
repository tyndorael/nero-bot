const Discord = require('discord.js');
const path = require('path');

module.exports = {
  name: 'kama',
  description: 'para el proximo pull',
  cooldown: 5,
  execute(message) {
    const embedMessage = new Discord.MessageEmbed()
      .setTitle('kama')
      .attachFiles([path.join(__dirname, './../assets/kama04.gif')])
      .setImage('attachment://kama04.gif');
    return message.channel.send(embedMessage);
  },
};
