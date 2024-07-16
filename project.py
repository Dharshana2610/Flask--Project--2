from flask import Flask
app=Flask(__name__)
@app.route('/')
def project():
    return "<h1 style='background:plum'><center>My first routing page</center></h1><hr><h2 style='color:olive'><center>The Boy Who Cried Wolf</center></h2><p style='color:Maroon'>There once was a boy who grew bored while watching over the village sheep. He wanted to make things more exciting. So, he yelled out that he saw a wolf chasing the sheep. All the villagers came running to drive the wolf away. However, they saw no wolf. The boy was amused, but the villagers were not. They told him not to do it again. Shortly after, he repeated this antic. The villagers came running again, only to find that he was lying. Later that day, the boy really sees a wolf sneaking amongst the flock. He jumped up and called out for help. But no one came this time because they thought he was still joking around. At sunset, the villagers looked for the boy. He had not returned with their sheep. They found him crying. He told them that there really was a wolf, and the entire flock was gone. An old man came to comfort him and told him that nobody would believe a liar even when they are being honest.<br><br><br><b>Moral:<br>Lying breaks trust.</p>"

@app.route('/abc')
def project1():
    return "<h1 style='background:plum'><center>My second page</center></h1><hr><h2 style='color:olive'><center>The Golden Egg</center></h2><p style='color:Maroon'>A farmer had a goose that laid one golden egg a day. He would sell the golden eggs, and they enjoyed a comfortable life. However, the farmer became greedy and wanted more than one egg a day. His wife foolishly agreed to his idea. The next day the farmer cut open the goose after it laid the golden egg. He could only find blood and guts. He realised his mistake. He now had no source of income, and the couple became poorer every day.<br><br><br><b>Moral:<br>Think before you act.</p>"

if __name__=='__main__':
    app.run(debug=True)