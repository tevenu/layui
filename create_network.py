import random  
import json

def get_random_color():  
    colors = [  
    "#F44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5", "#2196F3",  
    "#03A9F4", "#00BCD4", "#009688", "#4CAF50", "#8BC34A", "#CDDC39",  
    "#FFEB3B", "#FFC107", "#FF9800", "#FF5722", "#795548", "#9E9E9E",  
    "#607D8B", "#B71C1C", "#880E4F", "#4A148C", "#311B92", "#1A237E",  
    "#0D47A1", "#01579B", "#006064", "#004D40", "#1B5E20", "#33691E",  
    "#827717", "#F57F17", "#FF6F00", "#E65100", "#BF360C", "#3E2723",  
    "#212121", "#263238", "#1976D2", "#FFA000"  
    ]  
    return random.choice(colors)  
  
def get_random_in_range(min_val, max_val):  
    return random.uniform(min_val, max_val)  
  
def generate_random_nodes(num_nodes):  
    nodes = []  
    '''
    users = ["罗云熙Leo","Bunny小课堂","解说Kitty","瞳夕TXQQ","心态爆炸的大龄姨母","女足王霜","狂很子老","LNG_Hang","方从游中来",
             "Ale-胡嘉乐","解说瓜瓜","石头赶路ing","管泽元","彭立勋","LNG-scout","白宇WHITE","ssenming","我是郭杰瑞","ikussuki",
             "解说王淞","解说Kinko人","朱一龙","小米粥","年糕糕呀","陈欢","新浪游戏","解说Zonic","雨说体育徐静雨","楼盘黑衣人","YeGodzz",
             "圆某人和四某人","英超联赛","不能吃甜辣","张路评球","Wink0v0","AKUM","早安没吃饱","AkiXXXL","曼城足球俱乐部","默离"]
    '''
    '''
    users = ['体坛周报','萌宠百科','黄健翔','Rukia_wjy','周琦_26','zhuluojiong','马小良','冯潇','溜溜哥','赛车星冰乐',
            '我叫蓝姐','车手叶一飞','克总评车','狂飙客','韩寒','大油门的548','Superryry','Tommy12224','许子东','李武军',
            '曹亚旗','帅车评','巢巢巢巢巢Even','董路','李方妮','方正宇','崔岳2022','车手周冠宇','刘耀_FLy','老虎受欢迎',
            '疯狂历史','刘叔Joe','新水令','小灰羊是杨晓辉','庄宁宇','上海申花足球俱乐部','娄一晨','月上寻兔呀','羽毛球杂志','Kiya']
    '''
    users = ['植物眼','内含子','河森堡','折翼丛林','贼叉','天冬','ZKColorful','常岩CY','胡正阳','硬哥',
            '植物眼1','内含子1','河森堡1','折翼丛林1','贼叉1','天冬1','ZKColorful1','常岩CY1','胡正阳1','硬哥1',
            '植物眼2','内含子2','河森堡3','折翼丛林4','贼叉5','天冬6','ZKColorful8','常岩CY11','胡正阳12','硬哥13',
            '植物眼21','内含子21','河森堡13','折翼丛林41','贼叉51','天冬61','ZKColorful81','常岩CY111','胡正阳112','硬哥113']
    
    for i in range(num_nodes):  
        nodes.append({  
            "color": get_random_color(),  
            "label": users[i],  
            "attributes": {},  
            "y": get_random_in_range(-1000, 1000),  
            "x": get_random_in_range(-1500, 1500),  
            "id": users[i],  
            "size": get_random_in_range(0.5, 20)  
        })  
    nodes.append(
        {
            "color": get_random_color(),  
            #"label": "余霜YSCandice",  
            #"label": "我是F1车手兵哥",
            "label":"空中的士马宏",
            "attributes": {"关系":"本人"},  
            "y": 0,  
            "x": 0,  
            #"id": "我是F1车手兵哥",
            "id": "空中的士马宏",  
            "size": 20 
        }
    )
    return nodes  
  
def generate_random_edges(num_edges):  
    edges = []  
    '''
    users = ["罗云熙Leo","Bunny小课堂","解说Kitty","瞳夕TXQQ","心态爆炸的大龄姨母","女足王霜","狂很子老","LNG_Hang","方从游中来",
             "Ale-胡嘉乐","解说瓜瓜","石头赶路ing","管泽元","彭立勋","LNG-scout","白宇WHITE","ssenming","我是郭杰瑞","ikussuki",
             "解说王淞","解说Kinko人","朱一龙","小米粥","年糕糕呀","陈欢","新浪游戏","解说Zonic","雨说体育徐静雨","楼盘黑衣人","YeGodzz",
             "圆某人和四某人","英超联赛","不能吃甜辣","张路评球","Wink0v0","AKUM","早安没吃饱","AkiXXXL","曼城足球俱乐部","默离"]
    '''
    '''
    users = ['体坛周报','萌宠百科','黄健翔','Rukia_wjy','周琦_26','zhuluojiong','马小良','冯潇','溜溜哥','赛车星冰乐',
            '我叫蓝姐','车手叶一飞','克总评车','狂飙客','韩寒','大油门的548','Superryry','Tommy12224','许子东','李武军',
            '曹亚旗','帅车评','巢巢巢巢巢Even','董路','李方妮','方正宇','崔岳2022','车手周冠宇','刘耀_FLy','老虎受欢迎',
            '疯狂历史','刘叔Joe','新水令','小灰羊是杨晓辉','庄宁宇','上海申花足球俱乐部','娄一晨','月上寻兔呀','羽毛球杂志','Kiya']
    
    '''
    users = ['植物眼','内含子','河森堡','折翼丛林','贼叉','天冬','ZKColorful','常岩CY','胡正阳','硬哥',
            '植物眼1','内含子1','河森堡1','折翼丛林1','贼叉1','天冬1','ZKColorful1','常岩CY1','胡正阳1','硬哥1',
            '植物眼2','内含子2','河森堡3','折翼丛林4','贼叉5','天冬6','ZKColorful8','常岩CY11','胡正阳12','硬哥13',
            '植物眼21','内含子21','河森堡13','折翼丛林41','贼叉51','天冬61','ZKColorful81','常岩CY111','胡正阳112','硬哥113']
    
    for i in range(num_nodes):
        edges.append({
            #"sourceID": "余霜YSCandice",
            #"sourceID": "我是F1车手兵哥",
            "sourceID": "空中的士马宏",
            "attributes":{},
            "targetID": users[i],
            "size": 1
        })

    existing_edges = set()  
  
    while len(edges) < num_edges + num_nodes:  
        user_a = random.choice(users)  
        user_b = random.choice(users)  
    
        if user_a == user_b:  
            continue  
    
        edge_key = tuple(sorted([user_a, user_b]))  
    
        if edge_key in existing_edges:  
            continue  
    
        existing_edges.add(edge_key)  
    
        edges.append({  
            "sourceID": user_a,  
            "attributes": {},  
            "targetID": user_b,  
            "size": 0.5  
        }) 
    
    return edges  
  
num_nodes = 40 #其他节点个数  
num_edges = 100  
  
random_data = {  
    "nodes": generate_random_nodes(num_nodes),  
    "edges": generate_random_edges(num_edges)  
}  
  
with open('test_network3.json','w', encoding='utf-8') as file:
    json.dump(random_data, file, indent=2, ensure_ascii=False)