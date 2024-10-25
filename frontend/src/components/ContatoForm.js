import React, { useState } from 'react';
import api from '../api';

const ContatoForm = () => {
    const [email, setEmail] = useState('');
    const [telefone, setTelefone] = useState('');
    const [endereco, setEndereco] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const dados = { email, telefone, endereco };
        try {
            await api.post('/contato/', dados);
            alert('Contato salvo com sucesso!');
        } catch (error) {
            console.error("Erro ao salvar contato", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                E-mail:
                <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
            </label>
            <label>
                Telefone:
                <input type="tel" value={telefone} onChange={(e) => setTelefone(e.target.value)} />
            </label>
            <label>
                Endereço:
                <input type="tel" value={endereco} onChange={(e) => setEndereco(e.target.value)} />
            </label>
            <button type="submit">Enviar</button>
        </form>
    );
};

export default ContatoForm;
