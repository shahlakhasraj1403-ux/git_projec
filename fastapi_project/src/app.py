from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

mylist= [100, 200, 300]

@app.get('/home')
def say_hello():
    return{'HELLO':'WORLD'}


@app.get('/getItems/')
def get_items():
    return{'output':mylist}


@app.get('/lastItem')
def get_lastItem():
    if len(mylist) > 0:
        return{'output':mylist[-1]}
    else:
        return{'List Is Empty'}

    
@app.post('/addItem/{new_item}')
def insert_itrm(new_item:int):
    mylist.append(new_item)
    return{'new output': mylist}

@app.delete('/removeItem/')
def remove_item(item:int):
    if item in mylist:
        mylist.remove(item)
        return {'list after remove': mylist}
    else:
        return(f'{item} not found in list')



@app.delete('/popindex')
def remove_item(index:int):
    if index >= 0 and index < len(mylist):
        r= mylist.pop(index)
        return {f'{r} deleted from list'}
    else:
        return('index is worng')
   
@app.put('/updateItem/')
def update_item(index: int, new_item: int):
    if index >=0 and index < len(mylist):
        mylist [index] = new_item
        return {'updated list': mylist}
    else:
        return{f'index of {index}, not exist in my list'}

@app.put('/updateoldItem/')
def update_item(old_item:int, new_item: int ):
    if old_item in mylist:
        i = mylist.index(old_item)
        mylist[i] = new_item
        return{'list updated':mylist}
    else:
        return(f'{old_item} not found in list')