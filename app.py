#-------------------------------------------------------------------------------
# runserver.py
# Author: Gabriel Laniewski, Daniel MacLeod
#------------------------------------------------------------------------------

import os
from sys import argv, exit, stderr
import string
from collections import namedtuple
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

text = ["Artificial Intelligence, usually abbreviated as AI, refers to a variety of algorithms and programs which allow a machine to teach itself how to accomplish a specific task. This can be identifying trends in data, or teaching itself how to complete a complex task. What separates an AI from a traditional computer program is that the program does not tell the AI how to accomplish a specific task. The programmer instead creates a machine capable of learning how to do a task on its own, using either a dataset or feedback from a system. The importance of this distinction is twofold. First of all, an artificial intelligence can learn to complete tasks that we cannot formally express an algorithm for, such as a board game. Secondly, the same AI can be applied to a variety of different applications. ",
        "AI has already been adopted in a wide variety of settings. AI has found applications in such areas as robotics, planning and scheduling, process control, data mining, e-mail filtering, search engines, and speech recognition. Faced with an increasingly global and competitive business environment, organizations are seeking ways to improve their efficiency and effectiveness. The use of AI to improve decision making and achieve these goals is an important part of many organizations' efforts to increase their competitiveness and to gain a competitive edge.",
        "GPT-3 itself uses a form of AI known as deep learning, a relatively new model which is rapidly gaining in popularity. AI’s of this form were originally inspired by an organic brain, and have a complex net of simulated neurons which communicate with each other to produce highly sophisticated behavior. These Neurons are then trained using a wide selection of data to determine which connections are important in producing the desired outcome. GPT-3 has over 175 billion connections between its neurons, and was trained on over 600 billion training samples. It is considered state of the art, and can produce text that in most cases is indistinguishable from human writing. Unlike GPT-1 and GPT-2, GPT-3 is not open source as it was considered too powerful, and too likely to be abused (Tom B Brown et al).",
        "AI has already seen widespread adoption in society. The ease with which existing Ais can be repurposed by different groups has led to a huge array of creative applications. Some of which include: Adobe uses machine learning and AI to improve video editing, recognition and other functions. Amazon and Google use AI to improve search and provide better recommendations. Artificial intelligence helps doctors detect early signs of skin cancer. Google’s DeepMind AI defeated the world’s best Go player. Baidu, the equivalent of Google, is developing an autonomous vehicle. IBM Watson uses AI to help doctors diagnose and treat patients.",
        "As predicted by Kline and Pinch in “Users as Agents of Technological Change”, the users of AI have had a great deal of impact on how it is developed. AI was initially dominated by a model called a Support Vector Machine, which used complex linear equations to produce intelligent behavior. This model was widely liked by academics, as it could be concretely reasoned about and was mathematically elegant. The issue was that these models were not powerful enough for complex problems like image recognition. However, as large tech companies like Google started to put more data and computing power behind the project, deep learning models such as GPT-3 rapidly became more viable. These models required dramatically more computation power and larger training sets, but with the advent of the internet and the support of larger corporations these hurdles were cleared.",
        "Currently, the relevant social groups which use AI are mostly academics and larger corporations, as would be expected for a new and fairly complex technology. However, this broad overview fails to account for the small-scale use cases which will certainly become more important in the future. In academia, AI is seeing rapid adoption in fields outside of computer science. Economists and other social scientists are using AI to parse their huge datasets with greater accuracy than they could using conventional models. AI has also found success in experimental technologies across a variety of disciplines, such as AI powered ventilators that avoid damaging a patient's lungs. Another small, but notable group, are the hobbyists, and small businesses, who use AI for everything from video games to photo filters. These groups will only become larger as AI becomes more accessible and more widespread.",
        "In a world of attractive, free services, you are the product. Data harvesting from video hosting platforms like YouTube or social media sites such as Facebook is an extremely profitable business for these data brokers that get a large supply of your personal information for free. Respected authors such as Eric Posner and E. Glen Weyl in their book Radical Markets: Uprooting Capitalism and Democracy for a Just Society in fact argue that data broker companies are not compensating both their users and their employees a reasonable percentage of the value of the data collected. Artificial intelligence is crucial to mining this treasure trove of information--your private information goes from worthless to priceless with techniques such as natural language processing and data inference. ",
        "Modern applications of artificial intelligence have learned about a world centered around prejudices, racism, and inequalities that pervade a society with as many flaws as virtues. AI applications today are not able to reason, behave, or see the world as we do. We are not there yet. Luckily, the question of “when will we be able to learn to see the world like a machine” is a question of “how much time and money do we want to spend trying to get there?”. AI is something that can be engineered, and is not God-given. It is something that can be controlled and directed, and it is something that we can bring to justice. AI can be used to improve society and the lives of people. It can make the world a better place. But it is up to us to make it happen.",
        " If we’re not careful, AI is going to indelibly further existing biases in our society, such as the low-hanging bridges of Robert Moses meant to prevent low-income people from taking buses to affluent parks and neighborhoods, as described by Langdon Winner in his paper Do Artifacts Have Politics?. In addition, we’re already seeing ways in which AI systems can be used to perpetuate existing biases. For example, Google’s facial recognition tool — which is used in Google Photos — was found to be less accurate in identifying the faces of people of color than white faces. The company says it is working on improving the accuracy. Even more, researchers are using AI to predict and understand human behavior, including behavior that leads to mass killings. For example, researchers at the University of Washington recently used an AI system to predict which Twitter users might be more likely to commit mass homicides, based on their tweets.",
        "To regulate abuses of AI, what we need to regulate is not the technology itself, but instead the information which powers it. It is clear that in the modern age the data produced by our actions has monetary value, but it is bought and sold in a market with very few regulations, and that only a few elite parties have access to. Data is the lifeblood of any intelligent system. The software for artificial intelligences is relatively simple and often not proprietary. It is the vast reservoirs of data that are used to train these programs that have true value. Perhaps if more data collected both online and offline were more widely accessible, it could allow individuals and smaller organizations to fully use the power of AI, and also let the public know what information is being collected on them and how it could be used. What is certain is that this is definitely an area in which informed legislation is a must."
]

author = [True, False, True, False, True, True, True, False, False, True]

titles = ["Introduction", "Introduction", "Introduction", "Social Construction of Technology", "Social Construction of Technology", "Social Construction of Technology", "Dangers of AI", "Dangers of AI", "Politics and Technology", "Politics and Technology"]


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/<path:path>')
def catch_all(path):
    if "page" in path:
        page = int(path[4:6]) - 10
        score = int(path[9:])
        if page == 10:
            acc = int(((score-10)*100)/10)
            text2 = "We failed the Turing test..."
            if acc > 50:
                text2 = "The AI revolution draws closer..."
            if acc >= 80:
                text2 = "Looks like we are safe for now!"

            return render_template('end.html', score = score-10, text = text2, acc = acc)
        score1 = score
        score2 = score
        if author[page]:
            score1 += 1
        else:
            score2 += 1
        return render_template('para.html', title = titles[page], text = text[page], page = page+11, score1 = score1,  score2 = score2)
    return "<h1> 404 page not found </h1>"

if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        print(e, file=stderr)
        exit(1)
