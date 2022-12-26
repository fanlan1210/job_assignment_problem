# Job Assignment Problem

使用不同演算法來最佳化工作指派問題，目前只寫基因演算法，其他演算法有空再來補

## Run

```
python app.py
```

## 使用

把JAP問題的 N x N 表格放入 data.csv 中，再導入至 table 中產生 jap class，或使用 jap(N, MAX_VAL) 來產生 jap 物件

基因演算法參數如下
```
gaParameter = {
        'liveLoops' : 10,
        'jap' : japProblem,
        'popSize' : 5,
        'geneSize' : len(japProblem.timeTable),
        'mutationRate' : 0.1,  #變異率
        'mutationType' : mutation_type.Inversion,  #mutation_type.Inversion 
        'selectionType' : selection_type.Deterministic,
        'crossoverType' : crossover_type.PartialCrossover
    }
```

- liveloops : 基因的生命週期
- jap : 這邊要放jap物件
- popSize : 基因群數
- geneSize : 基因長度
- mutationRate : 變異率
- mutationType : 變異方法，可在 class mutation_type 中自定，預設兩種方法
  + mutation_type.Inversion : 挑一基因中一區間做反轉
  + mutation_type.Swap : 挑一基因兩點交換
- selectionType : 天擇方法，可在 selection_type 自定
  + Deterministic : 選擇 fitness 最好的基因
  + RouletteWheel : 是生是死全看運氣
- crossoverType : 交配方法，放在 crossover_type
  + PartialCrossover : 兩兩基因交配，方法爲選一區間[L, R]整段交換，產生兩個小孩，再去重

# figure 

用 matplotlib 畫的圖都存在 ./figure 下
- best : 有幾個 loops 就有幾張圖片，爲基因演算法每代當前的最佳答案所花費之成本
- minmax : 同 best ，內容改爲每代中最大和最小的成本
- every-loop-best.png : 每次基因演算法找到最佳解的值
