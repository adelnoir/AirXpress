# Dados fictícios
CLIENTES = [
    {"nome": "João Silva", "email": "joao.silva@email.com"},
    {"nome": "Maria Oliveira", "email": "maria.oliveira@email.com"},
    {"nome": "José Santos", "email": "jose.santos@email.com"},
    {"nome": "Ana Pereira", "email": "ana.pereira@email.com"},
    {"nome": "Carlos Rodrigues", "email": "carlos.rodrigues@email.com"},
    {"nome": "Margarida Alves", "email": "margarida.alves@email.com"},
    {"nome": "Bruno Ferreira", "email": "bruno.ferreira@email.com"},
    {"nome": "Cláudia Martins", "email": "claudia.martins@email.com"},
    {"nome": "Pedro Gonçalves", "email": "pedro.goncalves@email.com"},
    {"nome": "Beatriz Souza", "email": "beatriz.souza@email.com"}
]

AVIOES = [
    {"fabricante": "Boeing", "modelo": "747", "capacidade": 416},
    {"fabricante": "Airbus", "modelo": "A380", "capacidade": 555},
    {"fabricante": "Embraer", "modelo": "E190", "capacidade": 114},
    {"fabricante": "Bombardier", "modelo": "CRJ900", "capacidade": 90},
    {"fabricante": "Boeing", "modelo": "777", "capacidade": 396},
    {"fabricante": "Airbus", "modelo": "A320", "capacidade": 220},
    {"fabricante": "Embraer", "modelo": "E195", "capacidade": 124},
    {"fabricante": "Bombardier", "modelo": "CRJ700", "capacidade": 78},
    {"fabricante": "Boeing", "modelo": "787", "capacidade": 330},
    {"fabricante": "Airbus", "modelo": "A330", "capacidade": 290}
]

VOOS = [
    {"origem": "São Paulo", "destino": "Rio de Janeiro", "datahora_partida": "2024-12-10 14:00:00", 
     "datahora_chegada": "2024-12-10 15:30:00", "status": "planejado", "fk_aviao": 1},
    
    {"origem": "Lisboa", "destino": "Porto", "datahora_partida": "2024-12-11 09:00:00", 
     "datahora_chegada": "2024-12-11 10:00:00", "status": "em andamento", "fk_aviao": 2},
    
    {"origem": "Nova York", "destino": "Toronto", "datahora_partida": "2024-12-12 08:00:00", 
     "datahora_chegada": "2024-12-12 10:00:00", "status": "planejado", "fk_aviao": 3},
    
    {"origem": "Tóquio", "destino": "Seul", "datahora_partida": "2024-12-13 06:00:00", 
     "datahora_chegada": "2024-12-13 08:30:00", "status": "concluido", "fk_aviao": 4},
    
    {"origem": "Paris", "destino": "Londres", "datahora_partida": "2024-12-14 16:00:00", 
     "datahora_chegada": "2024-12-14 17:30:00", "status": "planejado", "fk_aviao": 2},
    
    {"origem": "Rio de Janeiro", "destino": "Buenos Aires", "datahora_partida": "2024-12-15 19:00:00", 
     "datahora_chegada": "2024-12-15 22:00:00", "status": "cancelado", "fk_aviao": 1},
    
    {"origem": "Sydney", "destino": "Auckland", "datahora_partida": "2024-12-16 07:00:00", 
     "datahora_chegada": "2024-12-16 12:00:00", "status": "em andamento", "fk_aviao": 5},
    
    {"origem": "Dubai", "destino": "Doha", "datahora_partida": "2024-12-17 20:00:00", 
     "datahora_chegada": "2024-12-17 21:30:00", "status": "concluido", "fk_aviao": 3},
    
    {"origem": "Frankfurt", "destino": "Zurique", "datahora_partida": "2024-12-18 11:00:00", 
     "datahora_chegada": "2024-12-18 12:00:00", "status": "planejado", "fk_aviao": 2},
    
    {"origem": "Los Angeles", "destino": "San Francisco", "datahora_partida": "2024-12-19 14:00:00", 
     "datahora_chegada": "2024-12-19 15:00:00", "status": "em andamento", "fk_aviao": 4}
]

RESERVAS = [
    {"fk_cliente": 1, "fk_voo": 1, "data": "2024-12-05 10:00:00"},
    {"fk_cliente": 2, "fk_voo": 2, "data": "2024-12-06 12:00:00"},
    {"fk_cliente": 3, "fk_voo": 3, "data": "2024-12-07 14:00:00"},
    {"fk_cliente": 4, "fk_voo": 4, "data": "2024-12-08 16:00:00"},
    {"fk_cliente": 5, "fk_voo": 5, "data": "2024-12-09 18:00:00"},
    {"fk_cliente": 6, "fk_voo": 6, "data": "2024-12-10 08:00:00"},
    {"fk_cliente": 7, "fk_voo": 7, "data": "2024-12-11 13:00:00"},
    {"fk_cliente": 8, "fk_voo": 8, "data": "2024-12-12 15:00:00"},
    {"fk_cliente": 9, "fk_voo": 9, "data": "2024-12-13 10:00:00"},
    {"fk_cliente": 10, "fk_voo": 10, "data": "2024-12-14 17:00:00"},
    {"fk_cliente": 1, "fk_voo": 2, "data": "2024-12-15 09:00:00"},
    {"fk_cliente": 2, "fk_voo": 3, "data": "2024-12-16 14:00:00"},
    {"fk_cliente": 3, "fk_voo": 4, "data": "2024-12-17 18:00:00"},
    {"fk_cliente": 4, "fk_voo": 5, "data": "2024-12-18 08:30:00"},
    {"fk_cliente": 5, "fk_voo": 6, "data": "2024-12-19 10:00:00"},
    {"fk_cliente": 6, "fk_voo": 7, "data": "2024-12-20 13:45:00"},
    {"fk_cliente": 7, "fk_voo": 8, "data": "2024-12-21 16:20:00"},
    {"fk_cliente": 8, "fk_voo": 9, "data": "2024-12-22 19:00:00"},
    {"fk_cliente": 9, "fk_voo": 10, "data": "2024-12-23 20:30:00"},
    {"fk_cliente": 10, "fk_voo": 1, "data": "2024-12-24 07:00:00"},
    {"fk_cliente": 1, "fk_voo": 5, "data": "2024-12-25 15:00:00"},
    {"fk_cliente": 6, "fk_voo": 10, "data": "2024-12-26 17:45:00"},
    {"fk_cliente": 4, "fk_voo": 2, "data": "2024-12-27 09:30:00"},
    {"fk_cliente": 8, "fk_voo": 6, "data": "2024-12-28 12:15:00"},
    {"fk_cliente": 3, "fk_voo": 7, "data": "2024-12-29 20:50:00"},
]
