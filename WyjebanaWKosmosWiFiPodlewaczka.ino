#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const int sensorPin1= 0;

char ssid[] = "xxx";                 // Network Name
char pass[] = "xxx";                 // Network Password
byte mac[6];

WiFiServer server(80);
IPAddress ip(x, x, x x);
IPAddress gateway(x, x, x, x);
IPAddress subnet(x, x, x, x);

WiFiClient client;
MySQL_Connection conn((Client *)&client);

char INSERT_SQL[] = "INSERT INTO abc(ID_PLANT, AIR_HUMIDITY, AIR_TEMPERATURE, SOIL_HUMIDITY) VALUES (1, NULL, NULL, %d)";
char query[128];

IPAddress server_addr(x, x ,x, x);    // MySQL server IP
char user[] = "xxxxx";           // MySQL user
char password[] = "xxxxx";       // MySQL password

void setup() {

  Serial.begin(9600);

  pinMode(sensorPin1, INPUT);

  Serial.println("Initialising connection");
  Serial.print(F("Setting static ip to : "));
  Serial.println(ip);

  Serial.println("");
  Serial.println("");
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.config(ip, gateway, subnet); 
  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi Connected");

  WiFi.macAddress(mac);
  Serial.print("MAC: ");
  Serial.print(mac[5],HEX);
  Serial.print(":");
  Serial.print(mac[4],HEX);
  Serial.print(":");
  Serial.print(mac[3],HEX);
  Serial.print(":");
  Serial.print(mac[2],HEX);
  Serial.print(":");
  Serial.print(mac[1],HEX);
  Serial.print(":");
  Serial.println(mac[0],HEX);
  Serial.println("");
  Serial.print("Assigned IP: ");
  Serial.print(WiFi.localIP());
  Serial.println("");

  Serial.println("Connecting to database");

  while (conn.connect(server_addr, 3306, user, password) != true) {
    delay(200);
    Serial.print ( "." );
  }

  Serial.println("");
  Serial.println("Connected to SQL Server!");  

}

void loop() {

  int soil_hum;

  soil_hum = 1024 - analogRead(sensorPin1);

  delay(10000); //10 sec

  sprintf(query, INSERT_SQL, soil_hum);

  Serial.println("Recording data.");
  Serial.println(query);
  
  MySQL_Cursor *cur_mem = new MySQL_Cursor(&conn);
  
  cur_mem->execute(query);

  delete cur_mem;

}