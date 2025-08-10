---
categories:
  - paper-reviews
date: "2024-07-23 00:00:00"
description: 논문 리뷰 - spark 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - paper-review
  - spark
thumbnail: assets/img/posts/2024-07-23-pyspark---how-to-preprocess-large-scale/thumbnail.jpg
title: Pyspark - How to preprocess Large Scale Data with Python
---

**논문 정보**

- **Date**: 2024-07-23
- **Reviewer**: 준원 장
- **Property**: spark

## 0. Prerequisites For Practice

- Spark runs on Java 8, 11, or 17.

- Install Apache Spark (Framework that powered the pyspark)

- Spark runs on Python 3.7+

- Install the following libraries in Python

```javascript
pip install pyspark findspark
conda install jupyter
```

- Launch jupyter lab in python

```javascript
jupyter - lab;
```

## 1. Introduction to Spark

### Spark

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-pyspark---how-to-preprocess-large-scale/image_000.png" class="img-fluid rounded z-depth-1" %}

- 대규모 데이터 처리를 위한 분석 엔진 (unified analytics engine for large-scale data processing)

- **In-Memory (RAM)** (Hadoop은 Disk에서 처리되기 때문에 여기서 속도차이가 발생)

- 분산 병렬처리

- 사용하기 쉬움

### MapReduce란?

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-pyspark---how-to-preprocess-large-scale/image_001.png" class="img-fluid rounded z-depth-1" %}

- Spark를 알기 위해서는 MapReduce라는거에 대해서 알면 매우 좋다

- **MapReduce는 대규모 데이터 세트를 처리하기 위한 프로그래밍 모델이자 구현 (i.e., distributed data processing)**

- 이름에도 명시되어 있듯이, 해당 모델은 두 가지 주요 단계, 즉 `Map` 단계와 `Reduce` 단계로 구성

_⇒ MapReduce 모델은 하둡(Hadoop)과 같은 시스템에서 널리 사용됨. 데이터를 디스크에 저장하고, 중간 결과도 디스크에 쓰기 때문에 대량의 데이터 처리에 적합하지만, 입출력 작업으로 인해 속도가 느려짐._

⇒ MapReduce는 YARN (Hadoop에서 사용되는 resource manager - CPU나 메모리 등의 계산 리소스가 관리되며, 아래 그림에서 어떤 호스트에 컨테이너를 어떻게 할당할 것인가를 결정)상에서 동작하는 분산 애플리케이션 중 하나며, 분산 시스템에서 데이터를 처리하는 데 사용됨.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-pyspark---how-to-preprocess-large-scale/image_002.png" class="img-fluid rounded z-depth-1" %}

⇒ 또한, SQL 같은 쿼리 언어를 위해 Apache Hive라는 쿼리 엔진을 사용할 수 있는데, 이들은 입력한 쿼리를 자동으로 MapReduce 프로그램으로 변환 해주기에 **아래 그림에서 확인할 수 있듯이 위 2개의 애플리케이션 (Hadoop, YARN) 모두 대량의 데이터를 배치 처리에 적합하지만, 애드 훅 쿼리를 여러 번 실행하는 복잡한 쿼리에는 부적합하며데이터 처리의 스테이지가 바꿜 때마다 약간의 대기 시간이 필요** (이건 Hive on Tez같은 기술적인 해결책이 존재)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-pyspark---how-to-preprocess-large-scale/image_003.png" class="img-fluid rounded z-depth-1" %}

⇒ 하지만 점점 RAM 가격이 저렴해졌고, (Disk IO로 빠질것을) In-Memory에서 돌아가는 SPARK 등장!

## 2. Spark (How Spark Work & Spark Session)

### How Spark Work

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-pyspark---how-to-preprocess-large-scale/image_004.png" class="img-fluid rounded z-depth-1" %}

- Spark는 기본적으로 multi-node (향후 글에서는 이를 **CLUSTER 모드/CLUSTER**라는 용어로 자주 사용됩니다!)에서 데이터를 처리하는 것을 원칙으로 함

- 따라서 해당 섹션에서는 CLUSTER 모드에서 Spark가 어떻게 동작하는지를 중점적으로 설명하나, 코드 실습은 환경적인 한계로 인해 단일노드 환경에서 진행했음을 양해해주시길 바랍니다

- Untitled 가 spark-submit이라는 resource를 얼마나 사용할지 config파일 같은 메뉴얼을 user code를 통해 제출하면 Driver Process에서 ‘Untitled ’을 생성

- 이때, 할당받은 Executor에서 실질적인 데이터가 처리됨

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-pyspark---how-to-preprocess-large-scale/image_005.png" class="img-fluid rounded z-depth-1" %}

- Spark 자체는 JVM으로 구동이 되지만, 다수의 언어가 Interface 형태로 지원됨!

### Spark Context vs. Spark Session

→ 이전에 Spark Session에 대해서 언급을 했는데, Spark Context라는 것도 있다. 둘의 차이를 알아보자

**#### Spark Context **

**#### Spark Session**

**##### Summary**

SparkContext를 사용하던 초기 Spark 버전에서는 주로 RDD(Resilient Distributed Datasets)를 사용하여 데이터를 처리. 이후에 조금 더 자세히 설명하겠지만 RDD는 Spark의 가장 기본적인 데이터 구조로, low-level API를 통해 데이터를 다루며, 큰 유연성을 제공하지만, 사용자가 많은 세부 사항을 직접 관리해야 하는 단점이 존재

Spark 2.0 이후 도입된 SparkSession은 DataFrame과 같은 high-level API를 제공함으로써, 사용자가 보다 쉽게 데이터를 구조화하고 SQL과 유사한 쿼리를 사용할 수 있게 해줌. 이 high-level API는 내부적으로 RDD를 사용하지만, 개발자가 직접 RDD를 다루는 것보다 훨씬 간단하고 효율적인 데이터 처리가 가능하도록 설계

### Spark의 Cluster 구성

→ Untitled 에서 어떻게 Spark가 구동되는지 간단히 알아보았으니, Spark가 작동되는 Cluster, 즉 multi-node 환경에서 실제로 앞서 설명한 노드들이 어떤 구조로 이루어져있는지, SparkSession과의 관계성도 고려해서 유기적으로 설명해보겠습니다.

1. **Master Node와 클러스터 매니저**

1. Untitled

## 3. RDDs (Resilient Distributed Datasets)

- Resilient Distributed Datasets (RDDs)는 Apache Spark의 핵심 데이터 구조로서, 분산 환경에서 대규모 데이터셋의 효율적인 처리를 가능

- SPARK라는 생태계의 가장 low-level의 데이터 처리 단위라고 필자는 이해하였다.

### About RDDs

1. **Backbone of data processing in Spark**

1. **Distributed, fault-tolerant, parallelizable data structure, and in-memory**

1. **Efficiently processes large datasets across a cluster**

1. **Key characteristics: immutable, distributed, resilient, lazily evaluated, fault-tolerant**:

### How to Make RDDs?

**#### **Untitled\*\* \*\*

```python
# Set the PySpark environment variables

import os
os.environ['SPARK_HOME'] = '/Users/name/App/Spark'
#  SPARK_HOME 환경 변수를 설정하여, PySpark가 Spark이 설치된 위치를 알 수 있도록 설정
os.environ['PYSPARK_DRIVER_PYTHON'] = 'jupyter'
# PYSPARK_DRIVER_PYTHON 환경 변수는 PySpark 세션을 시작할 때 어떤 Python 인터페이스를 사용할지 지정
os.environ['PYSPARK_DRIVER_PYTHON_OPTS'] = 'lab'
# PySpark가 Jupyter Lab을 실행할 때 필요한 추가 옵션을 제공
os.environ['PYSPARK_PYTHON'] = 'python'
# PYSPARK_PYTHON 환경 변수는 클러스터의 모든 노드에서 PySpark 작업을 처리할 때 사용할 Python 인터프리터를
# 이 설정은 PySpark가 작업을 분산 처리할 때 일관된 Python 환경을 유지하도록 돕습니다.
```

```python
from pyspark.sql import SparkSession
# Create a SparkSession
spark = SparkSession.builder.appName("RDD-Demo").getOrCreate()
```

```python

'''
현재 Spark 세션이 어떤 마스터 설정을 사용하고 있는지를 출력
### LOCAL
- local[*]이면 로컬 모드에서 모든 사용 가능한 코어를 사용하고 있다는 것을 의미
### CLUSTER
spark://host:port 형식이면 특정 클러스터 매니저(Standalone, Mesos, YARN 등)에 연결되어 있다는 것을 의미
'''
spark = SparkSession.builder.appName("RDD-Demo").getOrCreate()
print(spark.sparkContext.master)

# local[*]

'''
로컬 환경에서 실행 중인 경우, 스레드의 수(즉, 병렬 처리 가능한 작업의 수)는 다음과 같이 확인
'''
import multiprocessing

num_cores = multiprocessing.cpu_count()
print("Number of available cores:", num_cores)

# Number of available cores: 10
```

```python
# Data를 가용할 수 있는 core(CPU 코어들을 Worker 노드)중 5를 활용해 partitioning

numbers = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(numbers,5)

num_partitions = rdd.getNumPartitions()
print("Number of partitions:", num_partitions)

# glom() 함수를 사용하면 각 파티션의 데이터를 배열로 변환하여 파티션별로 그룹화
partitioned_data = rdd.glom().collect()

# print
print("Data in each partition:")
for i, data in enumerate(partitioned_data):
    print(f"Partition {i}: {data}")


# Data in each partition:
# Partition 0: [1]
# Partition 1: [2]
# Partition 2: [3]
# Partition 3: [4]
# Partition 4: [5]
```

```python
rdd.collect()
# [1, 2, 3, 4, 5]
```

**#### **Untitled\*\* \*\*

```python
from pyspark.sql import SparkSession

# 클러스터 모드에서 Spark 세션 설정
spark = SparkSession.builder \
    .master("spark://master_url:7077") \
    .appName("RDD-Demo") \
    .config("spark.executor.instances", "6") \ # 클러스터 전체에서 워커 노드들에 걸쳐 분배
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", "2") \
    .getOrCreate()


# RDD 생성 및 파티션 설정
numbers = list(range(1, 21))
rdd = spark.sparkContext.parallelize(numbers, 6)  # 명시적으로 파티션 수를 6으로 설정

# 각 파티션의 데이터를 리스트로 변환
partitioned_data = rdd.glom().collect()

# 출력
print("Data in each partition:")
for i, data in enumerate(partitioned_data):
    print(f"Partition {i}: {data}")


'''
(예상 출력 결과)
Data in each partition:
Partition 0: [1, 2, 3, 4]
Partition 1: [5, 6, 7, 8]
Partition 2: [9, 10, 11, 12]
Partition 3: [13, 14, 15, 16]
Partition 4: [17, 18]
Partition 5: [19, 20]
'''
```

### Transformations vs. Actions

- Transformation과 Action은 RDDs를 조작하고 결과를 도출하는 방법

- RDD operation은 Spark의 low-level API 작업이기에 `SparkSession`을 통해 접근 가능한 `SparkContext`의 인스턴스(`spark.sparkContext`)를 사용.

**#### Transformations**

- **개념**: Transformations은 RDD에 적용되는 연산으로, 새로운 RDD를 생성. _Transformations은 '지연 평가(lazy evaluation)' 모델을 따르기 때문에, 실제 연산은 관련된 동작(Action)이 호출될 때까지 실행X_

- **특성**: Transformations을 통해 생성된 새 RDD는 원본 RDD의 변경 불가능한(immutable) 특성을 유지하며, 원본 데이터를 수정하지 않고 새로운 데이터셋을 생성

- **예시**: `map`, `filter`, `flatMap`, `reduceByKey`, `sortBy`, `join` → `filter` 변환은 조건에 맞는 데이터만을 포함하는 새 RDD를 생성

**#### Actions**

- **개념**: Actions은 RDD에 적용되며, 변환된 데이터에 대해 계산을 실행하고 결과를 반환. Actions은 '적극적 평가(eager evaluation)'을 통해 즉시 결과를 도출

- **특성**: Actions은 Spark의 연산 과정에서 *lazy evaluation*된 transformations들을 trigger하고, 최종 결과를 계산하기 위해 데이터를 드라이버 프로그램으로 가져오거나 외부 시스템에 저장

- **예시**: `collect`, `count`, `first`, `take`, `save`, `foreach` → `collect` 동작은 RDD의 모든 요소를 드라이버 프로그램으로 반환하여 사용하도록 함

**#### Examples**

1. **Transformation**:

1. **Action**:

### Additional Operations

- `saveAsTextFile()`

- `textFile()`

## 4. DataFrame in Spark

### **DataFrames in Apache Spark**

- Spark DataFrame은 분산 데이터 컬렉션으로, 구조화된 데이터를 테이블 형태로 저장

- 각 컬럼에는 이름과 데이터 타입이 정의되어 있어 SQL 데이터베이스의 테이블과 유사

- RDD보다 high-level operation 수행가능, 직관적

**#### DataFrame Structure**
