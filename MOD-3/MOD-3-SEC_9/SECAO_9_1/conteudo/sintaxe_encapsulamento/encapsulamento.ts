// Exercício 5
// Altere a visibilidade dos atributos definidos na classe Tv para private.
class Tv {
    private _brand: string;
    private _size: number;
    private _resolution: string;
    private _connections: string[];
    private _connectedTo?: string;
  
    constructor(brand: string, size: number, resolution: string, connections: string[]) {
      this._brand = brand;
      this._size = size;
      this._resolution = resolution;
      this._connections = connections;
    }
  
    turnOn():void {
      console.log(
        `TV ${this._brand}, ${this._size}", resolution: ${this._resolution} \n\
  available connections: ${this._connections}`,
      );
    }

// Exercício 6
// Crie um método getter e um setter para o atributo _connectedTo, da classe Tv, de forma que:

// O setter deverá verificar se o valor definido está entre as conexões disponíveis (_connections) e:
// Em caso positivo, definir este valor para o atributo _connectedTo;
// Em caso negativo, imprimir no console a mensagem “Sorry, connection unavailable!”

    get connectedTo(): string | undefined {
        return this._connectedTo;
    }

    set connectedTo(value: string | undefined) {
        // permite setar undefined ou uma conexão que esteja no `connections`
        if (!value || this._connections.includes(value)) {
            this._connectedTo = value;
        console.log(this._connectedTo);
        } else {
          console.log('Sorry, connection unavailable!');
        }
    }
}

// Exercício 7
// Defina um valor para o atributo _connectedTo por meio do método setter criado e imprima seu valor.
const tv1 = new Tv('LG', 32, '4K', ['HDMI', 'Ethernet', 'Wifi']);
tv1.turnOn();
tv1.connectedTo = 'Wi-Fi';
console.log('Connected to: ', tv1.connectedTo);

