# L1 Neural Networks

## Structure

- **Input - hidden - output**
- **Input - hidden**
- **Input - hidden - output**
- **hidden**

## Perceptron

- Aims to **imitate the human brain**.
- Each perceptron takes multiple inputs and produces one output.

## Key Concepts

- **Activation Function**: Referred to as the function *f*.

## Process Flow

1. **Input, Weights, Sum, Non-Linearity, Output**
2. **Components**:
    - `x1` - `w1`
    - `x2` - `w2` - `Σ` - `Z` - `y`
    - `xm` - `wm`

- De gömda lagren är kärnan i ett NN
- Finns det många gömda lager kallas det deep neural network
- varje lager blir modellen mer komplex och olinjäritet kan fångas

Aktiveringsfunktioner
- Finns många 
- ReLU är bra go-to
- Stor påverkan på perceptronenens output
- Man kan använda olika aktiveringsfunktioner på olika ställen i nätverket
- Icke linjära aktiveringsfunktioner när man inte kan seperarea data med en linjär funktion

Inferrens av NN(Foward Pass)
- Input en datapunkt och beräkna alla steg genom hela nätverket tills du får en output
- input signals(values), input layer, 


- X: input vektor
- y: mål vektor (ground truth)
- y: output vektor
- L: antalet lager
- f1: activation funktion vid lager l

-w1 = (wljk): vikterna mellan lager l-1 och l, där (wljk) är vikten mellan k:te noden i lager l-1 och j:te noden i lager l.

Den totala ekvationen för nätverkeet blir då

g(x) := fL(WLFL-1(Wl1...f1(w1x)...))


För en datapunk i från träningsdatan {(xj, yi)}så beräknas outpen av nätverket enligt g(xj) = yi


Loss function:

Ett sätt att mäta hur fel vår output är jämfört med ground truth

Mean squareed Error MSE popular regressionsproblem, slå hårt på modelen ifall den gör fel.

Cross entropy loss är bra för klassiferings problem

Lossen för ett nätverk blir då L(yj, yj) = Loss [y hatt]


Bakåtpropagering (back propagation)

- Uppdaterar ett nätverk med avsseende på felet. Det gör att nätverket lär sig
- Vikterna i nätverket uppdateras och därmed lär sig modellen. 
-- vanligt att initisaeria vikterna till random bärden innnan tränning påbörjas 


Minima och Maxima y=f(x)
- lokla, maxima och minima
- globala, maxima och minima  

Dervata, lutning på kurvan på där vi är.

Gradient
- gradient är vetkor som pekar i riktning av skapraste lutningen i en funktion 
- ej att blanda ihop med derivata

Kedjeregeln.
For F(x) = f(g(x))
F'(x)= f'(g(x)).g'(x)

Derivatate of outer function f'
derivate of inner function g'

