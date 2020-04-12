package com.cesde.firebaseacademia;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.HashMap;
import java.util.Map;

public class Registro extends AppCompatActivity {
    EditText identif, nombres, correoe, telefono;
    Button registrar, iniciarsesion, buscar;
    FirebaseFirestore db;
    String idauto;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registro);
        identif = findViewById(R.id.etidentr);
        nombres = findViewById(R.id.etnombrer);
        correoe = findViewById(R.id.etcorreor);
        telefono = findViewById(R.id.ettelefonor);
        iniciarsesion = findViewById(R.id.btniniciarsesionr);
        registrar = findViewById(R.id.btnregistrarr);
        buscar = findViewById(R.id.btnbuscarr);
        //instanciar firabase firestore
        db = FirebaseFirestore.getInstance();
        //Evento clic del boton buscar
        buscar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                idauto = "";
                //
                db.collection("estudiante")
                        .whereEqualTo("identif", identif.getText().toString())
                        .get()
                        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                            @Override
                            public void onComplete(@NonNull Task<QuerySnapshot> task)
                            {
                                if (task.isSuccessful())
                                {
                                    for (QueryDocumentSnapshot document : task.getResult())
                                    {
                                        idauto = document.getId();
                                        //Log.d("prods", document.getId() + " => " + document.getData());
                                        identif.setText(document.getData().get("identif").toString());
                                        nombres.setText(document.getData().get("nombres").toString());
                                        correoe.setText(document.getData().get("correoe").toString());
                                        telefono.setText(document.getData().get("telefono").toString());
                                    }
                                    if (idauto.isEmpty())
                                    {
                                        Toast.makeText(getApplicationContext(), "Identificación no existe",Toast.LENGTH_SHORT).show();
                                    }
                                }
                                else
                                {
                                    Log.d("estudiante", "Error getting documents: ", task.getException());
                                }
                            }
                        });
                //
            }
        });


        //Evento clic del boton registrar
        registrar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Guardar
                Map<String, Object> estudiante = new HashMap<>();
                estudiante.put("identif",identif.getText().toString());
                estudiante.put("nombres",nombres.getText().toString());
                estudiante.put("correoe",correoe.getText().toString());
                estudiante.put("telefono",telefono.getText().toString());

                db.collection("estudiante")
                        .add(estudiante)
                        .addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
                            @Override
                            public void onSuccess(DocumentReference documentReference) {
                                //Log.d(TAG, "DocumentSnapshot added with ID: " + documentReference.getId());
                                Toast.makeText(getApplicationContext(), "Estudiante agregado correctamente",Toast.LENGTH_SHORT).show();

                            }
                        })
                        .addOnFailureListener(new OnFailureListener() {
                            @Override
                            public void onFailure(@NonNull Exception e) {
                                //Log.w(TAG, "Error adding document", e);
                                Toast.makeText(getApplicationContext(), "Error de conexion a la base de datos",Toast.LENGTH_SHORT).show();

                            }
                        });
                //Fin guardar
            }
        });
    }
}