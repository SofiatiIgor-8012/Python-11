# Verificando desconto
valor_compra = int(input("Digite o valor da compra: "))
cliente_vip = input("Voce e cliente VIP? (s/n): ")

# Basta ser VIP OU ter cupom para ganhar desconto
if valor_compra > 100 or cliente_vip == "s":
    print("Você tem direito ao frete grátis!")
else:
    print("Você não possui direito ao frete grátis")