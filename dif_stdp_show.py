from brian2 import *
import matplotlib.pyplot as plt

# Настройка модели
taupre = taupost = 20*ms
gmax = 0.01
dApre = 0.01
dApost = -dApre * 1.05  # Слегка асимметричный эффект для демонстрации
delta_ts = linspace(-50, 50, 100)*ms  # Различные временные интервалы между пред- и постсинаптическими спайками

# Список для хранения результатов
results = []

# Параметры для моделирования
lrs = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

for lr1, lr2 in lrs:
    w_changes = []
    for delta_t in delta_ts:
        # Инициализация модели
        start_scope()
        # Уравнения для STDP
        stdp_model = '''
        w : 1
        dApre/dt = -Apre / taupre : 1 (event-driven)
        dApost/dt = -Apost / taupost : 1 (event-driven)
        '''
        # События для пред- и постсинаптической активности
        on_pre = '''
        Apre += dApre
        w = clip(w + lr1*Apost, 0, gmax)
        '''
        on_post = '''
        Apost += dApost
        w = clip(w + lr2*Apre, 0, gmax)
        '''
        
        # Создание синапса
        G = NeuronGroup(2, 'v:1', threshold='t>(1+i)*10*ms', refractory=100*ms)
        S = Synapses(G, G, model=stdp_model, on_pre=on_pre, on_post=on_post)
        S.connect(i=0, j=1)
        S.w = gmax/2  # Начальный вес
        
        # Запуск модели
        run(10*ms + abs(delta_t), report='text')
        if delta_t > 0:
            run(delta_t)
        run(10*ms, report='text')
        
        # Сохраняем изменение веса
        w_changes.append(S.w[0] - gmax/2)
    
    results.append(w_changes)

# Визуализация результатов
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

for ax, result, lr in zip(axs.flatten(), results, lrs):
    ax.plot(delta_ts/ms, result)
    ax.set_title(f'lr1={lr[0]}, lr2={lr[1]}')
    ax.set_xlabel('Delta t (ms)')
    ax.set_ylabel('Change in synaptic weight')
    ax.axhline(0, ls='--', c='k', lw=1)
    ax.axvline(0, ls='--', c='k', lw=1)

plt.tight_layout()
plt.show()