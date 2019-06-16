---
layout: post
title:  "Il pendolo con elica"
subtitle: "Dinamica e controllo"
date:   2018-05-31 00:00:00 -0000
categories: controlli-automatici
imgpath: "/assets/post/pendolo-con-elica/img"
---

Questo progetto nasce dall'idea di controllare un pendolo tramite una coppia generata da un'elica solidale al corpo rigido, aumentando la difficoltà stessa del sistema di controllo, in quanto l'elica può soltanto spingere in un verso e quindi può generare soltanto una coppia positiva, e siamo costretti a sfruttare la forza di gravità come generatrice di coppia negativa.

Attenzione ! La realizzazione di questo progetto può risultare pericolosa! Vi suggerisco di prendere le giuste precauzioni, come spiegherò nelle sezioni successive.


## Il pendolo fisico

![My helpful screenshot]({{page.imgpath}}/physical_pendulum.jpg)

Il pendolo fisico è composto idealmente da un corpo rigido libero di ruotare attorno ad un centro di rotazione fissato al telaio. Il sistema meccanico ha un solo grado di libertà, e le equazioni del moto possono essere scritte come:

  $$
  \begin{eqnarray*}
      \dot{\theta}(t) &=& \omega(t) \\
      \dot{\omega}(t) &=& - \frac{mgL}{I_0}\sin\theta(t) - \beta\omega(t) + \frac{T(t)}{I_0}
  \end{eqnarray*}
   $$

dove

* $\theta(t)$ è l'angolo del corpo rigido rispetto alla posizione di riposo (vedi figura) [rad]
* $\omega(t)$ è la velocità angolare rispetto al centro di rotazione [rad/s]
* $m$ è la massa del corpo rigido [Kg]
* $g \approx 9.81$ è l'accelerazione di gravità [m/s^2]
* $L$ è la distanza tra il centro di rotazione e il centro di massa (CG) del corpo rigido [m]
* $I_{0}$ è il momento d'inerzia del corpo rigido rispetto al centro di rotazione [Kg*m^2]
* $\beta$ è il coefficiente di attrito viscoso
* $T(t)$ è la coppia esercitata sul corpo rigido [N*m]

L'inerzia rispetto al cenro di rotazione si può calcolare dall'inerzia del corpo rigido rispetto al suo centro di massa (CG) tramite la formula di [Huygens-Steiner](https://en.wikipedia.org/wiki/Parallel_axis_theorem)

$$I_0 = I_{CG} + mL^2$$

## 1.2 Linearized equations

State $x(t) = [x_1(t), x_2(t)] = [\theta(t), \omega(t)]$<br>
Input $u(t) = T(t)$ <br>
New state and input from the operating point $\bar{x}, \bar{u}$: 
$$\widetilde{x}(t) = x(t)-\bar{x}\\\widetilde{u}(t) = u(t)-\bar{u}$$


### Punto di equilibrio $\bar{x}=[0,0], \bar{u}=0,  \rightarrow \widetilde{u}(t)=u(t)=T(t)$



<table width="700" border="0">
  <tr>
    <td><img src="{{page.imgpath}}/pendulum_op_0_0.jpg"/></td>
    <td>
    <p>
    \[ \begin{bmatrix} \dot{\widetilde{x}}_1(t) \\ \dot{\widetilde{x}}_2(t) \end{bmatrix} =
       \begin{bmatrix}0 & 1\\-mgL/I_0 & -\beta\end{bmatrix} \begin{bmatrix} \widetilde{x}_1(t) \\ \widetilde{x}_2(t) \end{bmatrix} +
       \begin{bmatrix} 0 \\ 1/I_0 \end{bmatrix}\widetilde{u}(t)
    \]
    The transfer function between the angle $\widetilde{\Theta}(s)$ and the input $\widetilde{U}(s)$ is asymptotically stable (simply stable if $\beta=0$)
    
    \[ 
    	\frac{\widetilde{\Theta}(s)}{\widetilde{U}(s)}= \frac{1}{I_0}\frac{1}{s^2+\beta s+mgL/I_0}
    \]
    If $\beta \in (0,2\sqrt{mgL/I_0})$ then the system has two asymptotically stable complex poles:
    \[
    	\omega_n = \sqrt{\frac{mgL}{I_0}}, \zeta = \frac{\beta}{2 \omega_n}
    \]
    \[
    	p_{1,2} = \left(-\zeta \pm i\sqrt{\zeta^2-1}\right)\omega_n
    \]
    where $\omega_n, \zeta$ are the natural frequency and damping ratio respectively
    </p>
    
    </td>
  </tr>
</table>




### Punto di lavoro $\bar{x}=[\pi/2,0], \bar{u}=mgL, \rightarrow \widetilde{u}(t)=T(t)-mgL$


<table width="700" border="0">
  <tr>
    <td><img src="{{page.imgpath}}/pendulum_op_90_0.jpg"/></td>
    <td>
    <p>
    \[ \begin{bmatrix} \dot{\widetilde{x}}_1(t)  \\ \dot{\widetilde{x}}_2(t)  \end{bmatrix} =
       \begin{bmatrix}0 & 1\\0 & -\beta\end{bmatrix} \begin{bmatrix} \widetilde{x}_1(t)  \\ \widetilde{x}_2(t)  \end{bmatrix} +
       \begin{bmatrix} 0 \\ 1/I_0 \end{bmatrix}\widetilde{u}(t)
    \]
    
     The transfer function between the angle $\widetilde{\Theta}(s)$ and the input $\widetilde{U}(s)$ is given by
    
    \[ 
    	\frac{\widetilde{\Theta}(s)}{\widetilde{U}(s)}= \frac{1}{I_0}\frac{1}{s(s+\beta)}
    \]
    
    </p>
    
    </td>
  </tr>
</table>

### Punto di equilibrio $\bar{x}=[\pi,0], \bar{u}=0, \rightarrow \widetilde{u}(t)=u(t)=T(t)$

<table width="700" border="0">
  <tr>
    <td><img src="{{page.imgpath}}/pendulum_op_180_0.jpg"/></td>
    <td>
    <p>
    \[ \begin{bmatrix} \dot{\widetilde{x}}_1(t) \\ \dot{\widetilde{x}}_2(t) \end{bmatrix} =
       \begin{bmatrix}0 & 1\\mgL/I_0 & -\beta\end{bmatrix} \begin{bmatrix} \widetilde{x}_1(t) \\ \widetilde{x}_2(t) \end{bmatrix} +
       \begin{bmatrix} 0 \\ 1/I_0 \end{bmatrix}\widetilde{u}(t)
    \]
    
    The transfer function between the angle $\widetilde{\Theta}(s)$ and the input $\widetilde{U}(s)$ is unstable:
    
    \[ 
    	\frac{\widetilde{\Theta}(s)}{\widetilde{U}(s)}=  \frac{1}{I_0}\frac{1}{s^2+\beta s-mgL/I_0}
    \]
    
        If $\beta\ge 0$ then the system is unstable and the poles are given by:

    \[
    	p_{1,2} =\dfrac{-\beta \pm \sqrt{\beta^2+4mgL/I_0}}{2}
    \]
    
    
    
    </p>

    </td>
  </tr>
</table>
